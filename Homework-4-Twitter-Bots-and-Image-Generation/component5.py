from engine import GrammarEngine

def component5a():
  engine = GrammarEngine(file_path="grammars/5a.txt")
  for i in range(5):
    output = engine.generate(start_symbol_name="origin")
    for j in range(len(output) - 1):
      if output[j] + output[j+1] == "\\n":
       output = output[:j] + " \n" + output[j+2:]
    print(output)
  print("This looks wrong on replit but we promise its right paste it on Twitter")


def component5b():
  engine = GrammarEngine(file_path="grammars/5b.txt")
  for i in range(1):
    output = engine.generate(start_symbol_name="origin")
    for j in range(len(output) - 1):
      if output[j] + output[j+1] == "\\n":
       output = output[:j] + " \n" + output[j+2:]
    print(output)
  print("This one was specifically created for replit, so it only looks good on replit")

def component5c():
  engine = GrammarEngine(file_path="grammars/5c.txt")
  for i in range(1):
    output = engine.generate(start_symbol_name="origin")
    for j in range(len(output) - 1):
      if output[j] + output[j+1] == "\\n":
       output = output[:j] + " \n" + output[j+2:]
    print(output)
  print("This one was specifically created for replit, so it only looks good on replit")


def grade():
    """The function James will be using to grade your component."""
    print("\n\n-- Component 5a -- ")
    component5a()
    print("\n\n-- Component 5b -- ")
    component5b()
    print("\n\n-- Component 5c -- ")
    component5c()
