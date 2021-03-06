import time
from random import randrange
from grammar.engine import GrammarEngine
from rule_system.engine import RuleEngine

def component1():

  #creates a domain file and then opens and runs it  
  filename = f"rule_system/content/monkey_domain{int(time.time())}.txt"
  file = open(filename, "w") 

  #opens the grammar engine which will be used to generate the domain
  grammar_engine = GrammarEngine(
      file_path='grammar/grammars/monkey_grammar.txt',
      initial_state=None
    )
  #generates amount of monkeys, edible objects, and toys
  monk_count = randrange(3, 7) #3 to 6 monkeys are generated
  edible_count = randrange(1, 5) + monk_count #1-4 edible objects plus total amount of monkeys
  toy_count = randrange(0, 4) + monk_count #0-3 toys plus total number of monkeys

  #create the entity lines
  begin_entities = "<BEGIN ENTITIES>"
  end_entities = "<END ENTITIES>"
  begin_facts = "<BEGIN FACTS>"
  end_facts = "<END FACTS>"

  #create the entities 
    #these are the monkeys, creates the facts about them too
  monkey_entity = []
  monkey_facts = [] 

  for i in range (monk_count):
    name = grammar_engine.generate("Monkey")
    entity_hold =  name + ":Monkey"
    fact_hold = "<" + name + ">" + grammar_engine.generate("Location")
    if (entity_hold in monkey_entity):
      i -= 1
    else:
      monkey_entity.append(entity_hold)
      monkey_facts.append(fact_hold)

  #does same procedure for the food
  edible_entity = []
  edible_facts = []
  for i in range (edible_count):
    name = grammar_engine.generate("Food")
    entity_hold =  name + ":Banana"
    fact_hold = "<" + name + ">" + grammar_engine.generate("Edible")
    if (entity_hold in edible_entity):
      i -= 1
    else:
      edible_entity.append(entity_hold)
      edible_facts.append(fact_hold)
  
  toy_entity = []

  #same thing as before except toys don't have facts
  for i in range (toy_count):
    entity_hold = grammar_engine.generate("Objects") + ":Banana"
    if (entity_hold in toy_entity):
      i -= 1
    else:
      toy_entity.append(entity_hold)
  
  #builds the domain
  Domain = begin_entities
  for i in range (len(monkey_entity)):
    #starts a new line and then adds the monkey entitites
    Domain += "\n" + monkey_entity[i]
  
  for i in range (len(edible_entity)):
    #starts a new line and then adds the food entitites
    Domain += "\n" + edible_entity[i]
  for i in range (len(toy_entity)):
    #starts a new line and then adds the toy entitites
    Domain += "\n" + toy_entity[i]
  #moves from entities to the facts
  Domain += "\n" + end_entities
  Domain += "\n" + begin_facts
  for i in range (len(monkey_facts)):
    #starts a new line and then adds the monkey facts
    Domain += "\n" + monkey_facts[i]
  
  for i in range (len(edible_facts)):
    #starts a new line and then adds the food facts
    Domain += "\n" + edible_facts[i]
  #ends the facts section and then transfers it into a new file
  Domain += "\n" + end_facts

  #print(Domain)


  #adds the text to the file generated by the grammar engine
  file.write(Domain) 

  #closes the file
  file.close() 
  

  #runs the rule engine from the generated Domain File
  engine = RuleEngine(
  path_to_domain_file=filename,
  path_to_rules_file='rule_system/content/monkey_rules.txt',
  shuffle_randomly=True,
  random_seed=None)
  
  while not engine.produced_action(action_name="ActualEnd"):
      engine.execute(n=1)

  return filename



def grade():
    """The function James will be using to grade your component."""
    print("\n\n-- Component 1 -- ")
    component1()
