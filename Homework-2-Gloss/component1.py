from engine import TemplateEngine

def component1a():
  multi_line_output = ""
  engine = TemplateEngine(file_path="templates/C1.txt")
  for i in range(5):
      output = engine.generate(template_name="P1")
      multi_line_output += "\n" + output
  print(f"{multi_line_output}")

def component1b():
  multi_line_output = ""
  engine = TemplateEngine(file_path="templates/C1.txt")
  for i in range(5):
      output = engine.generate(template_name="P2")
      multi_line_output += "\n" + output
  print(f"{multi_line_output}")


def component1c():
  multi_line_output = ""
  engine = TemplateEngine(file_path="templates/C1.txt")
  for i in range(5):
      output = engine.generate(template_name="P3")
      multi_line_output += "\n" + output
  print(f"{multi_line_output}")



def component1d():
  multi_line_output = ""
  engine = TemplateEngine(file_path="templates/C1.txt")
  output = engine.generate(template_name="P1")
  multi_line_output += output
  output = engine.generate(template_name="P2")
  multi_line_output += output
  output = engine.generate(template_name="P3")
  multi_line_output += output
  output = engine.generate(template_name="P4")
  multi_line_output += output
  print(f"{multi_line_output}")


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