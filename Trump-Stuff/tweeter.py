from engine import GrammarEngine

def tweeter():
  engine = GrammarEngine(file_path="corpora/Sentence.txt")
  print("@RealDonaldTrump tweeting here:")
  for i in range(5):
      print(engine.generate(start_symbol_name="1"))