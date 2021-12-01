from engine import GrammarEngine

def component4():
  engine = GrammarEngine(file_path="grammars/c4.txt")
  for i in range(10):
      print(engine.generate(start_symbol_name="SENTENCE"))


def grade():
    """The function James will be using to grade your component."""
    print("\n\n-- Component 4 -- ")
    component4()


#4a) "A Little Train" — he chose this because kids books can be simple enough to form sentences but sophisticated enough to use full real words that follow syntax rules. 

#4b) It was particularly interesting because Yngve made sentences that were generated in some way but still made syntactic and grammatical sense.