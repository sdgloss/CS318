from engine import GrammarEngine

def component1a():
  engine = GrammarEngine(file_path="grammars/c1.txt")
  for i in range(5):
      print(engine.generate(start_symbol_name="1a"))


def component1b():
  engine = GrammarEngine(file_path="grammars/c1.txt")
  for i in range(5):
      print(engine.generate(start_symbol_name="1b"))


def component1c():
  engine = GrammarEngine(file_path="grammars/c1.txt")
  for i in range(5):
      print(engine.generate(start_symbol_name="1c"))


def component1d():
  engine = GrammarEngine(file_path="grammars/c1.txt")
  for i in range(3):
      print(engine.generate(start_symbol_name="1d"))
      print("\n------------------------\n")


def grade():
    """The function James will be using to grade your component."""
    print("\n\n-- Component 1a -- ")
    component1a()
    print("\n\n-- Component 1b -- ")
    component1b()
    print("\n\n-- Component 1c -- ")
    component1c()
    print("\n\n-- Component 1d -- ")
    component1d()