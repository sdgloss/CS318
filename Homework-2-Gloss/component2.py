from engine import TemplateEngine

def component2a():
  multi_line_output = ""
  for i in range(5):
      engine = TemplateEngine(file_path="templates/C2.txt", random_seed=16)
      output = engine.generate(template_name="P1")
      multi_line_output += "\n" + output
  print(f"{multi_line_output}")


def component2b():
  multi_line_output = ""
  engine = TemplateEngine(file_path="templates/C2.txt")
  for i in range(10):
      output = engine.generate(template_name="PROBABILISTIC")
      multi_line_output += "\n" + output
  print(f"{multi_line_output}")


def component2c():
  multi_line_output = ""
  engine = TemplateEngine(file_path="templates/C2.txt")
  for i in range(10):
      output = engine.generate(template_name="P3")
      multi_line_output += "\n" + output
  print(f"{multi_line_output}")


def component2d():
  multi_line_output = ""
  engine = TemplateEngine(file_path="templates/C2.txt")
  for i in range(10):
      output = engine.generate(template_name="P4")
      multi_line_output += "\n" + output
  print(f"{multi_line_output}")


def component2e():
  multi_line_output = ""
  engine = TemplateEngine(file_path="templates/C2.txt")
  for i in range(10):
      output = engine.generate(template_name="P1")
      output = " " + output[1:].capitalize()
      multi_line_output += "\n" + output
  print(f"{multi_line_output}")


def component2f(): 
  multi_line_output = ""
  engine = TemplateEngine(file_path="templates/C2.txt")
  for i in range(10):
      output = engine.generate(template_name="CONJUGATION")
      hold = output.split(" ")
      vowels = ["a","e","i","o","u"]
      for j in range(len(hold) - 1):
        if hold[j] == "an" and hold[j+1][0] not in vowels:
          hold[j] = "a"
        elif hold[j] == "a" and hold[j+1][0] in vowels:
          hold[j] = "an"
      output = " ".join(hold)
      multi_line_output += "\n" + output
  
  print(f"{multi_line_output}")


def component2g():
  multi_line_output = ""
  engine = TemplateEngine(file_path="templates/C2.txt")
  for i in range(10):
      output = engine.generate(template_name="P7")
      for j in range(len(output) - 1):
        if output[j] + output[j+1] == "\\n":
          output = output[:j] + " \n" + output[j+2:]
      multi_line_output += "\n" + output
  print(f"{multi_line_output}")


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
    print("\n\n-- Component 2e -- ")
    component2e()
    print("\n\n-- Component 2f -- ")
    component2f()
    print("\n\n-- Component 2g -- ")
    component2g()
