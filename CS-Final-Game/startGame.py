from grammar.engine import GrammarEngine
from rule_system.engine import RuleEngine
from hero import hero as stud
from location import location


def startGame():
  #set up domainfile
  setDomain()
  #set up map
  loc = setMap()
  #set up the game
  rulez = game()
  #set up hero
  hero = setHero(rulez, loc)
  #runs the game
  print("Welcome to Sadness world. A world dominated by dragons. You are a lowly drunk who has no money or hope for the booze he truely desires. Today, you have decided to bring back hope where there is none and maybe even fight off the dragon. Will you free the kingdom or will you die trying?")
  runGame(hero, rulez)

  
def setDomain():
  #intializes the hero domain so it isn't editted 
  filename1 = f"rule_system/content/hero/hero_domain.txt"
  filename2 = f"rule_system/content/updated_hero/hero_domain.txt"
  file1 = open(filename1, "r")
  string = file1.read()
  file2 = open(filename2, "w")
  file2.write(string)
  file1.close()
  file2.close()

def setHero(rule_engine, location):
  hero = stud(rule_engine, location)
  return hero
  

def setMap():
  #sets all of the map locations
  drawBridge = location("draw bridge", True, ["fight", "examine"])
  brothel = location("brothel", True, ["hint"])
  volcano = location("volcano", False, ["examine", "fight"])
  ghostTown = location("ghost town", True, ["examine", "shoot"])
  poisonFog = location("poison fog", True, ["examine", "throw"])
  library = location("library", False, ["fight", "examine", "pull", "read"])
  #greatSea = location("great sea", True, ["examine", "throw"])
  sands = location("sands", False, ["fight","examine"])
  grass = location("grass", True, ["fight","examine"])
  #plains = location("plains", False, ["examine"])
  #marsh = location("marsh", True, ["fight", "examine"])

  #connects the different spots in the game
  spots = [brothel,grass,drawBridge,sands,poisonFog,library,ghostTown]
  brothel.connect(grass)
  grass.connect(brothel)
  grass.connect(drawBridge)
  drawBridge.connect(grass)
  drawBridge.connect(sands)
  sands.connect(drawBridge)
  sands.connect(poisonFog)
  sands.connect(ghostTown)
  poisonFog.connect(sands)
  poisonFog.connect(library)
  library.connect(poisonFog)
  ghostTown.connect(sands)
  #sands.connect(plains)
  #plains.connect(sands)
  #plains.connect(marsh)
  #marsh.connect(plains)
  #marsh.connect(greatSea)
  #greatSea.connect(marsh)
  #greatSea.connect(volcano)
 # volcano.connect(greatSea)

  return spots


def game():
  rule_engine = RuleEngine(
        path_to_domain_file='rule_system/content/updated_hero/hero_domain.txt',
        path_to_rules_file='rule_system/content/all_locations_rules.txt',
        shuffle_randomly=True,
        random_seed=None
    )
  return rule_engine
  

def setSpot(file, filepath, grammarpath):
  
  engine = RuleEngine(
  path_to_domain_file=file,
  path_to_rules_file=filepath,
  shuffle_randomly=True,
  random_seed=None)
  spot = location.init(engine, grammarpath, filepath)

  return spot
  
def runGame(hero, rule_engine):
  while not rule_engine.produced_action(action_name="End1"):
      runMove(hero)
      while not rule_engine.produced_action(action_name="Waiting"):
        rule_engine.execute(n=1)
      rule_engine.execute(n=1)
      hero.check_moveable()
      
      
      

def runMove(hero):
  going = True
  while(going):
    action = input("What would you like to do? (help for options, remember no caps in this game)")
    holder = hero.cur_location_node().run()
    holder2 = []
    for i in range(len(holder)):
      holder2.append(holder[i].name())
    if (action == "help"):
      holder = hero.cur_location_node().options
      print("Here are your options:")
      for i in range(len(holder)):
        print(holder[i])
    elif (action in hero.cur_location_node().movez):
      hero.do_action(action)
      going = False
    elif (action == "moves"):
      holder = hero.cur_location_node().movez
      print("Here are your move choices:")
      for i in range(len(holder)):
       print(holder[i])
    elif(action == "run"):
      print("Here is where you can move:")
      for i in range(len(holder)):
        print(holder[i].name())
    elif(action in holder2):
      hero.run(action)
    elif(action == "equip"):
      hero.equip(input("what would you like to equip"))
    elif(action == "inventory"):
      hero.check_inventory()
    elif(action == "location"):
      print(hero.current_location())
    else:
      print("invalid entry: remember just say location name to go somewhere")
