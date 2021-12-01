from engine import TemplateEngine

def component6():
  multi_line_output = ""
  engine = TemplateEngine(file_path="templates/C6.txt")
  for i in range(5):
      output = engine.generate(template_name="P1")
      for j in range(len(output) - 1):
        if output[j] + output[j+1] == "\\n":
          output = output[:j] + " \n" + output[j+2:]
      print(f"{output}")
      print("---------------------")
  


def grade():
    """The function James will be using to grade your component."""
    print("\n\n-- Component 6 -- ")
    component6()


#a) can't only use one word once, instead after it's used, could be called again from the text list

#b) add it into a dictionary then see if the word is used by putting a % sign in front of the words as notation so the engine knows to only use the word once.  