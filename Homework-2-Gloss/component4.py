from engine import TemplateEngine
def component4():
  multi_line_output = ""
  engine = TemplateEngine(file_path="templates/C4.txt")
  for i in range(5):
      output = engine.generate(template_name="P1")
      for j in range(len(output) - 1):
        if output[j] + output[j+1] == "\\n":
          output = output[:j] + " \n" + output[j+2:]
      multi_line_output += "\n--------------\n" + output
  print(f"{multi_line_output}")


def grade():
    """The function James will be using to grade your component."""
    print("\n\n-- Component 4 -- ")
    component4()

#A) Computers use a pseudo-random number sequence that is generated from a seed number, so though the number is not truely random, the human eye cannot tell the difference. Thus, the results should end up pretty similar from both sequences although the longer the string of random letters the more likely you are to guess the computers next letter. 

#B) so lets say a letter has frequency of 5% then you would type it in 5 time, or if it has a frequency of 1, you type it in once, for a total of 100 lettters. More precision means more total letters and letters used.

#C) Currently, that would make us call on a seperate template for each letter recursively, which our templates right now can't do. With more sophositicated letters though it would be easy to make happen, you just plug in the associated frequency's with all 27 chars and go nuts. 

