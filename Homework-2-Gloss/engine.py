import random


class TemplateEngine:
    """An engine for template-based text generation.

    Attributes:
        templates:
            A list of Template objects, one for each template in the given template definitions file.
    """

    def __init__(self, file_path, random_seed=None):
        """Initialize a TemplateEngine object.
        
        Args:
            file_path:
                A string containing the path to a template definitions file in the expected format.
            random_seed:
                A value that will be used to seed the random module. If None is passed, no seed 
                will be used. Look up random seeds if you're not familiar with the notion.
        """
        # Parse the template definitions file located at the given file path
        self.templates = self._parse_template_definition_file(file_path=file_path)
        # If we received a random seed, use it to seed the random module
        if random_seed is not None:
            random.seed(random_seed)

    def _parse_template_definition_file(self, file_path):
        """Parse the template definitions file at the given file path.

        Note: I use a leading underscore in this method name to cue that it is a private method, meaning that it
        should never be called except by this object's other instance methods. While some languages, like Java,
        require an explicit declaration of whether a method is private, in Python the leading underscore is just
        a convention that is meant to make the code more readable. Some IDEs, like PyCharm, will also issue a
        warning when a private method is called from outside its class. Finally, this docstring conforms to the
        Google Python Style Guide: https://github.com/google/styleguide/blob/gh-pages/pyguide.md#383-functions-
        and-methods. I don't always conform to this style guide, but in this case I do. One nice thing about using
        it for docstrings is that IDEs like PyCharm recognize the format and can use it to help you debug.

        Args:
            file_path:
                A string containing the path to a template definitions file in the expected format.

        Returns:
            A list of Slot objects and a list of Template objects.

        Raises:
            IOError:
                An error occurred accessing the template definitions file.
        """
        # Read in the raw template definitions. If there's no file at this path, or if the path is otherwise
        # malformed, an IOError will be raised. Note that the template definitions include both slot and
        # template definitions.
        template_definitions = open(file_path).read()
        # Parse the slot definitions to form a Slot object for each defined slot
        slots = self._parse_slot_definitions(template_definitions=template_definitions)
        # Parse the template definitions to form a Template object for each defined template. Note how this
        # requires access to the list of Slot objects that we just created -- this is why we parsed the slot
        # definitions first, and it's also why I place the definition for the method _parse_slot_definitions()
        # before that of _parse_template_definitions.
        templates = self._parse_template_definitions(template_definitions=template_definitions, slots=slots)
        return templates

    def _parse_slot_definitions(self, template_definitions):
        """Parse the slot definitions included in the given template definitions file content.

        Args:
            template_definitions:
                A string containing the contents of a template definitions file.

        Returns:
            A list of Slot objects.

        Raises:
            AssertionError:
                The template definitions file does not conform to the expected format.
            Exception:
                There is a malformed slot definition in the template definitions file, or two slots with the
                same name.
        """
        # First, make sure that the template definitions file is in the expected format. We'll do this using
        # Python's 'assert' statement, which raises an AssertionError if the condition in the left side of the
        # comma evaluates to False, in which case the error message on the right side of the comma will be printed.
        # This form of validation will be used throughout the process of parsing the template definitions.
        assert "<BEGIN SLOTS>" in template_definitions, "Template definitions file missing '<BEGIN SLOTS>'."
        assert "<END SLOTS>" in template_definitions, "Template definitions file missing '<END SLOTS>'."
        assert template_definitions.index("<BEGIN SLOTS>") < template_definitions.index("<END SLOTS>"), (
            "'<BEGIN SLOTS>' comes after <END SLOTS> in template definitions file."
        )
        # Extract the slot definitions by taking the substring between the index of the start marker ("<BEGIN SLOTS>")
        # and the end marker ("<END SLOTS>"). Note that the str.index() function returns the index of the first
        # character of the first instance of the substring that is passed to it; as such, we'll add to the start
        # index the length of the start marker, so that we don't include the marker itself in the extracted content.
        slot_definitions_start_index = template_definitions.index("<BEGIN SLOTS>") + len("<BEGIN SLOTS>")
        slot_definitions_end_index = template_definitions.index("<END SLOTS>")
        slot_definitions = template_definitions[slot_definitions_start_index:slot_definitions_end_index]
        # Next, iterate over each line in the slot definitions to attempt to form a Slot object for any line that
        # doesn't consists of non-whitespace characters or begin with '#' (our comment symbol). We'll append each
        # Slot object to the list of slots.
        slots = []
        for line in slot_definitions.split('\n'):
            line = line.lstrip()  # Remove all leading whitespace on the line
            if not line:  # The line contained only whitespace, so now it's an empty string
                continue  # Move on to the next iteration of the 'for' loop, i.e., to the next line
            if line.startswith('#'):  # It's a comment
                continue
            while '\t\t' in line:  # Replace consecutive tab characters with a single tab character
                line = line.replace('\t\t', '\t')
            # If we get to here, this must be a slot definition, though it may be malformed. Here, we'll use
            # a try-except block to safely attempt to parse it as if it were in the expected format. If it's
            # not in the expected format, i.e., it doesn't have two fields separated by a single tab, a
            # ValueError will be raised indicating that splitting on the tab character did not produce exactly
            # two components. If this happens, we'll raise an Exception with an error message including the
            # malformed slot definition.
            try:
                slot_name, slot_values_str = line.split('->')
            except ValueError:
                # Let's form a nice error message that includes the exact slot definition that was malformed. We'll
                # do this using a Python f-String (http://zetcode.com/python/fstring/).
                if '->' not in line:
                    error_message = f"Malformed slot definition (no '->' delimiter): '{line}'"
                else:  # It has too few or too many components; there should be exactly two: name and values
                    error_message = f"Malformed slot definition: '{line}'"
                raise Exception(error_message)
            # At this point, there's two ways that this slot definition could be malformed: 1) the slot name is an
            # empty string or comprises only whitespace, or 2) the slot-values component is an empty string or
            # comprises only whitespace. We'll check for both and raise an Exception, with an informative error
            # message, in each case.
            slot_name = slot_name.strip()  # Remove leading or trailing whitespace
            slot_values_str = slot_values_str.strip()
            if not slot_name:  # It comprised only whitespace
                error_message = f"Slot definition includes no name: {line}"
                raise Exception(error_message)
            if not slot_values_str:  # It comprised only whitespace
                error_message = f"Slot definition includes no values: {line}"
                raise Exception(error_message)
            # If we got to here, we successfully parsed out the slot name and slot values. Next, we'll parse the
            # list of values; this is simply a comma separated list. Note that calling str.split(delimiter) on a
            # string that doesn't include the delimiter is just fine -- it will just return the entire string.
            raw_slot_values = slot_values_str.split(',')
            # Some of these values may be commands to load in the contents of a corpus file, so let's iterate
            # over them one by one to check. If we find a corpus reference, we'll remove that from the slot values
            # and append to the slot values every element in the referenced corpus.
            slot_values = []
            for raw_slot_value in raw_slot_values:
                if not raw_slot_value.startswith('$'):
                    # It's a regular slot value, so append it to the list of slot values and move onto the 
                    # next iteration of the loop
                    slot_values.append(raw_slot_value)
                    continue
                corpus_filename = raw_slot_value[1:]  # Remove the leading dollar sign
                corpus_values = self._load_corpus(corpus_filename=corpus_filename)
                slot_values += corpus_values
            # Finally, instantiate a Slot object for this slot definition and append it to the list of Slot objects
            slot_object = Slot(name=slot_name, values=slot_values)
            slots.append(slot_object)
        # As a final check, make sure that there's no cases of two slots having the same name
        for slot in slots:
            for other_slot in slots:
                if slot is not other_slot:  # They're not literally the same object (this is what 'is' checks for)
                    if slot.name == other_slot.name:
                        raise Exception(f"Multiple slots with the name '{slot.name}'.")
        return slots

    @staticmethod
    def _load_corpus(corpus_filename):
        """Return the contents of a corpus loaded from a corpus file.

        Note: I use the decorator '@staticmethod' because this instance method does not require access to
        the instance's data, i.e., there is no point to passing the 'self' argument, since it's not used
        anywhere in the method. While Python has formal support for 'static' methods like this one, I'm
        using here as a convention that makes the code easier to understand; for example, by using the
        decorator, I express to you that this method will not -- and, in fact, cannot -- modify the object
        instance's attributes via side effects.

        Args:
            corpus_filename:
                The filename for the corpus that's to be loaded.

        Returns:
            A list of strings.

        Raises:
            IOError:
                There is no corpus file with the given name in the 'corpora' folder.
        """
        return open(f"corpora/{corpus_filename}").read().split('\n')

    def _parse_template_definitions(self, template_definitions, slots):
        """Parse the actual template definitions included in the given template definitions file content.

        Note: the procedure used here closely follows that of _parse_slot_definitions(), and so the comments
        here are not as verbose, since they assume you've already read the comments for the earlier method.
        Which is to say, consult the comments in _parse_slot_definitions() if you're having trouble understanding
        what's going on here.

        Another note: I don't use '@staticmethod' here because this method calls another instance method,
        _parse_template_definitions(), and to access this other method, the method needs the 'self' argument
        to be passed (so that the instance can call 'self._parse_template_definitions()').

        Args:
            template_definitions:
                A string containing the contents of a template definitions file.

        Returns:
            A list of Template objects.

        Raises:
            AssertionError:
                The template definitions file does not conform to the expected format.
            Exception:
                There is a malformed template definition in the template definitions file.
        """
        # First, make sure that the template definitions file is in the expected format
        assert "<BEGIN TEMPLATES>" in template_definitions, "Template definitions file missing '<BEGIN TEMPLATES>'."
        assert "<END TEMPLATES>" in template_definitions, "Template definitions file missing '<END TEMPLATES>'."
        assert template_definitions.index("<BEGIN TEMPLATES>") < template_definitions.index("<END TEMPLATES>"), (
            "'<BEGIN TEMPLATES>' comes after <END TEMPLATES> in template definitions file."
        )
        # Extract the template definitions
        template_definitions_start_index = template_definitions.index("<BEGIN TEMPLATES>") + len("<BEGIN TEMPLATES>")
        template_definitions_end_index = template_definitions.index("<END TEMPLATES>")
        template_definitions = template_definitions[template_definitions_start_index:template_definitions_end_index]
        # Next, iterate over each line in the template definitions to attempt to form a Template object for any line
        # that doesn't consists of non-whitespace characters or begin with '#' (our comment symbol). We'll append each
        # Template object to the list of slots.
        templates = []
        for line in template_definitions.split('\n'):
            line = line.lstrip()  # Remove all leading whitespace on the line
            if not line:  # The line contained only whitespace, so now it's an empty string
                continue  # Move on to the next iteration of the 'for' loop, i.e., to the next line
            if line.startswith('#'):  # It's a comment
                continue
            # If we get to here, this must be a slot definition, though it may be malformed. Again, we'll use
            # a try-except block to safely attempt to parse it as if it were in the expected format.
            try:
                template_name, template_definition = line.split('->')
            except ValueError:
                error_message = f"Malformed template definition: '{line}'"
                raise Exception(error_message)
            # At this point, here's two ways that this template definition could be malformed: 1) the template name
            # is an empty string or comprises only whitespace, or 2) the actual template component is an empty string
            # or comprises only whitespace. We'll check for both and raise an Exception, with an informative error
            # message, in each case.
            template_name = template_name.strip()  # Strip off surrounding whitespace, possibly leaving an empty string
            if not template_name:
                error_message = f"Template definition includes no name: {line}"
                raise Exception(error_message)
            if not template_definition.strip():
                error_message = f"Template definition includes no values: {line}"
                raise Exception(error_message)
            # Now, let's parse the template definition to form a list representing the template. This list
            # will contain strings (for the static elements in the template) and also Slot objects (for the slots
            # in the template). To form such a list, we need to separate the slots from the static elements. This
            # can be done in one line using a regular expression (i.e., the Python 're' module), but I assume that
            # you haven't learned about those yet, so instead we'll iterate through the template string one
            # character at a time. This will take several lines, during which we'll also retrieve any Slot objects
            # referenced in the template, so let's break into a new method to preserve the granularity and readability
            # of this one.
            template = self._parse_template_definition(template_definition=template_definition, slots=slots)
            # Finally, instantiate a Template object for this template definition and append it to the list of
            # template objects
            template_object = Template(name=template_name, template=template)
            templates.append(template_object)
        # As a final check, make sure that there's no cases of two templates having the same name
        for template in templates:
            for other_template in templates:
                if template is not other_template:
                    if template.name == other_template.name:
                        raise Exception(f"Multiple templates with the name '{template.name}'.")
        return templates

    @staticmethod
    def _parse_template_definition(template_definition, slots):
        """Parse the given template definition.

        Args:
            template_definition:
                A string containing a raw template definition. For example: "<DET> <NOUN> <VERB>. The end.".

        Returns:
            A list containing both strings (template static elements) and Slot objects (template slots), in the
            order in which they are included in the template definition.

        Raises:
            Exception:
                The template definition references a slot that has not been defined.
        """
        template = []  # This will be populated with strings (static elements) and Slot objects (slots)
        # Iterate over the template definition, one character at a time, looking specifically for the angle
        # brackets that demarcate slots in the template.
        iterating_over_slot_name = False
        slot_name = None
        static_element = ''
        for character in template_definition:
            if iterating_over_slot_name:
                if character != '>':  # We're still iterating over the slot name, so append this character
                    slot_name += character
                else:  # We've hit the end of the slot name...
                    iterating_over_slot_name = False
                    # Now we need to retrieve the Slot object associated with this name. If there isn't one, we'll
                    # treat this template definition as being malformed (since there's no way to fill it in), and raise
                    # an Exception now to cue the authoring error.
                    try:
                        slot_object = next(slot for slot in slots if slot.name == slot_name)
                    except StopIteration:  # There is no slot by that name in the 'slots' list
                        error_message = (
                            f"Template definition '{template_definition}' references an undefined slot '{slot_name}'."
                        )
                        raise Exception(error_message)
                    template.append(slot_object)
            elif character == '<':  # We've hit the beginning of a slot name
                # If there was a static element preceding this slot, append it to the template
                if static_element:
                    template.append(static_element)
                    static_element = ''
                iterating_over_slot_name = True
                slot_name = ''
            else:  # We must be iterating over a static element
                static_element += character
        # Even though we're done iterating over the template definition, there may have been a static element
        # at the end of it, which we would have failed to have added to the template. Let's make sure to do
        # that here.
        if static_element:
            template.append(static_element)
        return template

    def generate(self, template_name):
        """Use the template with the given name to generate a single text output.

        This method relies on Template.generate() to do most of the work, but it's handy in that it allows
        one to call that method for any template whose name is known. This can be used to easily assemble
        the outputs of various templates.

        Args:
            template_name:
                A string, being the name of the template that is to be used to generate a text output.

        Returns:
            A string, being a single text output produced by filling the slots in the template with the given name.

        Raises:
            Exception:
                There is no defined template with the given name.
        """
        # First, we need to retrieve the Template object associated with this name. If there isn't one, we'll
        # elect to raise an Exception to let the caller know.
        try:
            template_object = next(template for template in self.templates if template.name == template_name)
        except StopIteration:  # There is no defined template by that name, so raise an Exception
            error_message = f"There is no defined template with the name {template_name}. "
            all_defined_template_names = ", ".join(template.name for template in self.templates)
            error_message += f"These templates are defined: {all_defined_template_names}."
            raise Exception(error_message)
        # If we retrieved a Template object, use it to generate a single text output, and return that
        output = template_object.generate()
        return output


class Template:
    """A template, for use in template-based text generation.

    Attributes:
        name:
            A string, being the template name.
        template:
            A list of strings (static elements) and Slot objects (slots).
    """

    def __init__(self, name, template):
        """Initialize a Slot object.

        Args:
            name:
                A string, being the template name.
            template:
                A list of strings (static elements) and Slot objects (slots).
        """
        self.name = name
        self.template = template

    def generate(self):
        """Use this template to generate a single text output.

        Returns:
            A string, being a single text output produced by filling the slots in this template.
        """
        output = ''
        for element in self.template:
            if isinstance(element, Slot):  # It's a slot, so append one of its values
                # Here, we'll use the Slot method 'fill()', which returns a random value
                output += element.fill()
            else:  # It's a static element, so append it as is
                output += element
        return output


class Slot:
    """A slot in a template, for use in template-based text generation.

    Attributes:
        name:
            A string, being the slot name.
        values:
            A list of strings, each being one way of filling the slot.
    """

    def __init__(self, name, values):
        """Initialize a Slot object.

        Args:
            name:
                A string representing the slot name.
            values:
                A list of strings, each being one way of filling the slot.
        """
        self.name = name
        self.values = values

    def fill(self):
        """Fill this slot.

        This method fills the slot by randomly selecting from the list of slot values. Of course, we could
        modify this method to implement a different policy, such as using each slot value one at a time, with
        no repeating until every value has been used once.

        Returns:
            A string representing one way to fill the slot.
        """
        return random.choice(self.values)
