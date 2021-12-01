from engine import GrammarEngine


def generate():
    """Generate an output without 'debug' mode on."""
    # Prepare a grammar engine using the "basic.txt" grammar file
    engine = GrammarEngine(file_path="grammars/basic.txt")
    # Generate an output, with debug printout showing each
    # step in its derivation
    output = engine.generate(start_symbol_name="SENTENCE", debug=False) 
    print(output)


def debug():
    """Generate an output with 'debug' mode on."""
    # Prepare a grammar engine using the "basic.txt" grammar file
    engine = GrammarEngine(file_path="grammars/basic.txt")
    # Generate an output, with debug printout showing each
    # step in its derivation
    engine.generate(start_symbol_name="SENTENCE", debug=True)


def state_usage_demo():
    """Generate content that makes use of the engine state."""
    # Prepare a grammar engine using the "state.txt" grammar file
    engine = GrammarEngine(file_path="grammars/test.txt")
    # Generate a "story" in which random elements recur. This is
    # made possible by writing to and reading from the engine state.
    output = engine.generate(start_symbol_name="ACT1", debug=False)
    print(f"{output}\n")
    # Finally, print out the contents of the engine state after the
    # generation instance (if debug=True above, this will be printed)
    # at the beginning and at the end of the generation isinstance,
    # in which case there's no point to call it again here.
    engine.inspect_state()
    # To export the engine state (for use in another engine), use
    # the following method
    exported_state = engine.export_state()
    # To clear the engine state (prior to a subsequent call to 
    # engine.generate(), if you want a fresh state for that call),
    # use this method
    engine.clear_state()
