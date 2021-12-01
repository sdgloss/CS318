from grade import grade
from engine import TemplateEngine


def demo():
    """James's demo functionality from our class session on 9/21."""
    # Prepare a template engine -- this is what fills in templates,
    # given all template and slot definitions in
    # "templates/basic_templates.txt".
    engine = TemplateEngine(file_path="templates/basic_templates.txt")
    # Write out ten lines that are generated from the template called
    # "SENTENCE"
    for i in range(10):
        output = engine.generate(template_name="SENTENCE")
        print(f"{i}\t{output}")


def multi_line_output():
    """James's demo functionality from our class session on 9/23."""
    # Prepare a template engine -- this is what fills in templates,
    # given all template and slot definitions in
    # "templates/basic_templates.txt".
    engine = TemplateEngine(file_path="templates/basic_templates.txt")
    # Write out ten lines that are generated from the template called
    # "SENTENCE"
    multi_line_output = ""
    for i in range(4):
        output = engine.generate(template_name="SENTENCE")
        multi_line_output += "\n" + " " * i + output
    print(f"{multi_line_output}")


#demo()

# Uncomment this function to print out all your results, at any time (see grade.py)
grade()
