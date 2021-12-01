from engine import TemplateEngine

def component8a():
  multi_line_output = ""
  engine = TemplateEngine(file_path="templates/C8.txt")
  for i in range(5):
      output = engine.generate(template_name="QUATRAIN")
      for j in range(len(output) - 1):
        if output[j] + output[j+1] == "\\n":
          output = output[:j] + " \n" + output[j+2:]
      multi_line_output += "\n--------------\n" + output
  print(f"{multi_line_output}")


def component8b():
  multi_line_output = ""
  engine = TemplateEngine(file_path="templates/C8.txt")
  for i in range(5):
      output = engine.generate(template_name="Limerick")
      for j in range(len(output) - 1):
        if output[j] + output[j+1] == "\\n":
          output = output[:j] + " \n" + output[j+2:]
      multi_line_output += "\n--------------\n" + output
  print(f"{multi_line_output}")


def component8c():
  multi_line_output = ""
  engine = TemplateEngine(file_path="templates/C8.txt")
  for i in range(5):
      output = engine.generate(template_name="Haiku")
      for j in range(len(output) - 1):
        if output[j] + output[j+1] == "\\n":
          output = output[:j] + " \n" + output[j+2:]
      multi_line_output += "\n--------------\n" + output
  print(f"{multi_line_output}")


def grade():
    """The function James will be using to grade your component."""
    print("\n\n-- Component 8a -- ")
    component8a()
    print("\n\n-- Component 8b -- ")
    component8b()
    print("\n\n-- Component 8c -- ")
    component8c()
