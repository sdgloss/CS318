from engine import TemplateEngine
def component5a():
  multi_line_output = ""
  engine = TemplateEngine(file_path="templates/Magic_Plot_Scale.txt")
  for i in range(5):
      output = engine.generate(template_name="P1")
      for j in range(len(output) - 1):
        if output[j] + output[j+1] == "\\n":
          output = output[:j] + " \n" + output[j+2:]
      multi_line_output += "\n--------------\n" + output
  print(f"{multi_line_output}")



def component5b():
  multi_line_output = ""
  engine = TemplateEngine(file_path="templates/Magic_Plot_Scale.txt")
  for i in range(5):
      output = engine.generate(template_name="P2")
      multi_line_output += "\n--------------\n" + output
  print(f"{multi_line_output}")


def grade():
    """The function James will be using to grade your component."""
    print("\n\n-- Component 5a -- ")
    component5a()
    print("\n\n-- Component 5b -- ")
    component5b()
