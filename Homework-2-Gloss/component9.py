from engine import TemplateEngine

def component9():
  multi_line_output = ""
  engine = TemplateEngine(file_path="templates/C9.txt")
  for i in range(5):
      output = engine.generate(template_name="LETTER")
      for j in range(len(output) - 1):
        if output[j] + output[j+1] == "\\n":
          output = output[:j] + " \n" + output[j+2:]
      multi_line_output += "\n--------------\n" + output
  print(f"{multi_line_output}")


def grade():
    """The function James will be using to grade your component."""
    print("\n\n-- Component 9 -- ")
    component9()
