from engine import GrammarEngine

def component5():
  engine = GrammarEngine(file_path="grammars/c5.txt")
  print(engine.generate(start_symbol_name="MAIN"))


def grade():
    """The function James will be using to grade your component."""
    print("\n\n-- Component 5 -- ")
    component5()

