from grammar.engine import GrammarEngine
from rule_system.engine import RuleEngine
from component1 import component1
import time


def challenge1():
    # Here's some code to append the contents of one file
    # to another, which you can adapt to create a new
    # rules file with your original hand-authored rules along
    # with your procedurally generated ones.
    filepath = f"rule_system/content/monkey_rules{int(time.time())}.txt"
    file = open(filepath, "w")
        # Read in the contents of your original rules file
    content = open("rule_system/content/monkey_rules.txt").read()
    grammar_engine = GrammarEngine(
            file_path='grammar/grammars/monkey_rules_grammar.txt',
            initial_state=None,
            random_seed=None
        )
    all_rules_str = ""       
    for _ in range(3):
            new_rule_str = grammar_engine.generate(start_symbol_name="MonkeyRule")
            new_rule_str = form(new_rule_str)
            all_rules_str += new_rule_str + "\n"
    all_rules_str += content
    file.write(all_rules_str)
    file.close
    engine = RuleEngine(
    path_to_domain_file= component1(),
    path_to_rules_file= filepath,
    shuffle_randomly=True,
    random_seed=None)
    n = 0
    while (n < 1):
      engine.execute(n)
      n += 1

def form(thing):
  holder = ""
  i=0
  while (i < (len(thing) - 1)):
    if(thing[i] == "%"):
      holder += "$"
    elif (thing[i] + thing[i+1] == "/n"):
      holder += "\n"
      i+=1
    else:
      holder += thing[i]
    i+= 1
  holder += thing[len(thing) -1] + "\n"
  return holder


def grade():
    """The function James will be using to grade your component."""
    print("\n\n-- Supplementary Challenge 1 -- ")
    challenge1()
