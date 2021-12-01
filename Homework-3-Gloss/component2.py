from engine import GrammarEngine
def component2a():
  engine = GrammarEngine(file_path="grammars/c2.txt")
  for i in range(3):
      print(engine.generate(start_symbol_name="2a"))


def component2b():
  engine = GrammarEngine(file_path="grammars/c2.txt")
  for i in range(3):
      print(engine.generate(start_symbol_name="INDIRECT_REFERENCE"))


def component2c():
  engine = GrammarEngine(file_path="grammars/c2.txt")
  for i in range(3):
      print(engine.generate(start_symbol_name="ACT_1"))
      print(engine.generate(start_symbol_name="ACT_2"))
      print("\n------------------------\n")


def component2d():
    initial_state = {'second_name' :'Sam', 'action': 'Bam',  'reciever': 'Lam'}
    engine = GrammarEngine(file_path = "grammars/c2.txt",initial_state = initial_state)
    print(engine.generate(start_symbol_name="2d"))



def grade():
    """The function James will be using to grade your component."""
    print("\n\n-- Component 2a -- ")
    component2a()
    print("\n\n-- Component 2b -- ")
    component2b()
    print("\n\n-- Component 2c -- ")
    component2c()
    print("\n\n-- Component 2d -- ")
    component2d()
