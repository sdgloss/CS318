from engine import TemplateEngine

def component7a():
  multi_line_output = ""
  engine = TemplateEngine(file_path="templates/C7.txt")
  for i in range(10):
      output = engine.generate(template_name="7a")
      multi_line_output += "\n" + output
  print(f"{multi_line_output}")


def component7b():
  multi_line_output = ""
  engine = TemplateEngine(file_path="templates/C7.txt")
  for i in range(10):
      output = engine.generate(template_name="7b")
      multi_line_output += "\n" + output
  print(f"{multi_line_output}")


def component7c():
  multi_line_output = ""
  engine = TemplateEngine(file_path="templates/C7.txt")
  for i in range(10):
      output = engine.generate(template_name="7c")
      mirror = output.split(" ")
      mirror.reverse()
      mirror = " ".join(mirror)
      multi_line_output += "\n" + output + " whereas " + mirror
  print(f"{multi_line_output}")


def grade():
    """The function James will be using to grade your component."""
    print("\n\n-- Component 7a -- ")
    component7a()
    print("\n\n-- Component 7b -- ")
    component7b()
    print("\n\n-- Component 7c -- ")
    component7c()
