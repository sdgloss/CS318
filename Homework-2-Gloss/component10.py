from engine import TemplateEngine

def component10():
  multi_line_output = ""
  engine = TemplateEngine(file_path="templates/C10.txt")
  for i in range(5):
      output = engine.generate(template_name="P1")
      for j in range(len(output) - 1):
        if output[j] + output[j+1] == "\\n":
          output = output[:j] + " \n" + output[j+2:]
      multi_line_output += "\n--------------\n" + output
  print(f"{multi_line_output}")


def grade():
    """The function James will be using to grade your component."""
    print("\n\n-- Component 10 -- ")
    component10()
