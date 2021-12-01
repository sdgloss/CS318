from engine import GrammarEngine

def component9():
  #disclaimer, on this part I found that I was frustrated with the fact I couldn't do append string values so I decided to build a street fighter like game that will append string values. 
  engine = GrammarEngine(file_path="grammars/c9.txt")
  for i in range(3):
    runGame(engine)
    print("\n ---------------")
      

def runGame(engine):
    print(engine.generate(start_symbol_name="Start"))
    health1 = 100
    health2 = 100
    while (True):
      print(engine.generate(start_symbol_name = "Battle_1"))
      lostH = int(engine.generate(start_symbol_name = "damHold2"))
      health2 -= lostH
      if (health2 < 1):
        print(engine.generate(start_symbol_name = "Faint2"))
        break
      else:
        print(engine.generate(start_symbol_name = "Battle_2"))
        lostH = int(engine.generate(start_symbol_name = "damHold1"))
        health1 -= lostH
        if (health1 < 1):
          print(engine.generate(start_symbol_name = "Faint1"))
          break
      update = {'char1' : engine.generate(start_symbol_name = "char1"), 'char2' : engine.generate(start_symbol_name = "char2"), 'rHealth1' : str(health1), 'rHealth2': str(health2)}
      engine = GrammarEngine(file_path="grammars/c9.txt", initial_state = update)
      print(engine.generate(start_symbol_name = 'RemainingHealth1'))
      print(engine.generate(start_symbol_name = 'RemainingHealth2'))
      


def grade():
    """The function James will be using to grade your component."""
    print("\n\n-- Component 9 -- ")
    component9()
