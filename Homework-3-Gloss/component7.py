from engine import GrammarEngine
import component6

def component7():
    # engine = component6.return_engine()
    screenplay_engine = component6.component6()
    screenplay_state = screenplay_engine.export_state()
    print("\n\n-- Component 7 -- ")
    synopsis_engine = GrammarEngine(file_path="grammars/c7.txt", initial_state=screenplay_state)
    print(synopsis_engine.generate(start_symbol_name="Synopsis"))



def grade():
    """The function James will be using to grade your component."""
    component7()
