from engine import GrammarEngine

d = {}
pub_engine = GrammarEngine(file_path="grammars/c6.txt")

def component6():
  engine = GrammarEngine(file_path="grammars/c6.txt")
  engine.generate(start_symbol_name="Name1")
  engine.generate(start_symbol_name="Name2")
  print(engine.generate(start_symbol_name="Scene_Heading"))
  print("\n" + engine.generate(start_symbol_name="Action_1"))
  print("\n" + "(" + engine.generate(start_symbol_name="Parantheticals") + ")")
  print("\n" + engine.generate(start_symbol_name="Dialogue_1"))
  print("\n" + engine.generate(start_symbol_name="Dialogue_12"))
  print("\n" + engine.generate(start_symbol_name="Dialogue_13"))
  print("\n" + engine.generate(start_symbol_name="Dialogue_14"))
  print("\n" + engine.generate(start_symbol_name="Dialogue_15"))
  print("\n" + engine.generate(start_symbol_name="Dialogue_16"))
  print("\n" + engine.generate(start_symbol_name="Dialogue_17"))
  print("\n" + engine.generate(start_symbol_name="Dialogue_18"))
  print("\n" + engine.generate(start_symbol_name="Dialogue_19"))
  print("\n" + engine.generate(start_symbol_name="Dialogue_10"))
  print("\n" + engine.generate(start_symbol_name="Transitions"))
  print(engine.generate(start_symbol_name="Scene_Heading"))
  print("\n" + engine.generate(start_symbol_name="Action_2"))
  print("\n" + "(" + engine.generate(start_symbol_name="Parantheticals") + ")")
  print("\n" + engine.generate(start_symbol_name="Dialogue_2"))
  print("\n" + engine.generate(start_symbol_name="Dialogue_21"))
  print("\n" + engine.generate(start_symbol_name="Dialogue_22"))
  print("\n" + engine.generate(start_symbol_name="Dialogue_23"))
  print("\n" + engine.generate(start_symbol_name="Dialogue_24"))
  print("\n" + engine.generate(start_symbol_name="Dialogue_25"))
  print("\n" + engine.generate(start_symbol_name="Dialogue_26"))
  print("\n" + engine.generate(start_symbol_name="Dialogue_27"))
  print("\n" + engine.generate(start_symbol_name="Dialogue_28"))
  print("\n" + engine.generate(start_symbol_name="Dialogue_29"))
      
  print("\n" + engine.generate(start_symbol_name="Transitions"))
  print(engine.generate(start_symbol_name="Scene_Heading"))
  print("\n" + engine.generate(start_symbol_name="Action_3"))
  print("\n" + "(" + engine.generate(start_symbol_name="Parantheticals") + ")")
  print("\n" + engine.generate(start_symbol_name="Dialogue_3"))
  print("\n" + engine.generate(start_symbol_name="Dialogue_31"))
  print("\n" + engine.generate(start_symbol_name="Dialogue_32"))
  print("\n" + engine.generate(start_symbol_name="Dialogue_33"))
  print("\n" + engine.generate(start_symbol_name="Dialogue_34"))
  print("\n" + engine.generate(start_symbol_name="Dialogue_35"))
  print("\n" + engine.generate(start_symbol_name="Dialogue_36"))
  print("\n" + engine.generate(start_symbol_name="Dialogue_37"))
  print("\n" + engine.generate(start_symbol_name="Dialogue_38"))
  print("\n" + engine.generate(start_symbol_name="Dialogue_39"))
  print("\n" + engine.generate(start_symbol_name="Transitions"))
  print(engine.generate(start_symbol_name="Scene_Heading"))
  print("\n" + engine.generate(start_symbol_name="Action_4"))
  print("\n" + "(" + engine.generate(start_symbol_name="Parantheticals") + ")")
  print("\n" + engine.generate(start_symbol_name="Dialogue_4"))
  print("\n" + engine.generate(start_symbol_name="Dialogue_41"))
  print("\n" + engine.generate(start_symbol_name="Dialogue_42"))
  print("\n" + engine.generate(start_symbol_name="Dialogue_43"))
  print("\n" + engine.generate(start_symbol_name="Dialogue_44"))
  print("\n" + engine.generate(start_symbol_name="Dialogue_45"))
  print("\n" + engine.generate(start_symbol_name="Dialogue_46"))
  print("\n" + engine.generate(start_symbol_name="Dialogue_47"))
  print("\n" + engine.generate(start_symbol_name="Dialogue_48"))
  print("\n" + engine.generate(start_symbol_name="Dialogue_49"))
  
  print("\n" + engine.generate(start_symbol_name="Transitions"))


  print(engine.generate(start_symbol_name="Scene_Heading"))
  print("\n" + engine.generate(start_symbol_name="Action_5"))
  print("\n" + "(" + engine.generate(start_symbol_name="Parantheticals") + ")")
  print("\n" + engine.generate(start_symbol_name="Dialogue_5"))
  print("\n" + engine.generate(start_symbol_name="Dialogue_51"))
  print("\n" + engine.generate(start_symbol_name="Dialogue_52"))
  print("\n" + engine.generate(start_symbol_name="Dialogue_53"))
  print("\n" + engine.generate(start_symbol_name="Dialogue_54"))
  print("\n" + engine.generate(start_symbol_name="Dialogue_55"))
  print("\n" + engine.generate(start_symbol_name="Dialogue_56"))
  print("\n" + engine.generate(start_symbol_name="Dialogue_57"))
  print("\n" + engine.generate(start_symbol_name="Dialogue_58"))
  print("\n" + engine.generate(start_symbol_name="Dialogue_59"))
  print("\n" + engine.generate(start_symbol_name="Endings"))
  update_slots(engine)
  return engine


def update_slots(engine):
  d['name1'] = engine.generate(start_symbol_name ="Get_Name1")
  d['name2'] = engine.generate(start_symbol_name ="Get_Name2")
  d['action'] = engine.generate(start_symbol_name ="Get_Action")
  d['action1'] = engine.generate(start_symbol_name ="Get_Action1")
  d['action2'] = engine.generate(start_symbol_name ="Get_Action2")
  d['action3'] = engine.generate(start_symbol_name ="Get_Action3")
  d['action4'] = engine.generate(start_symbol_name ="Get_Action4")
  d['action5'] = engine.generate(start_symbol_name ="Get_Action5")
  d['animal'] = engine.generate(start_symbol_name ="Get_Animal")
  d['sport'] = engine.generate(start_symbol_name ="Get_Sport")
  d['outcome'] = engine.generate(start_symbol_name ="Get_Outcome")
  d['wMove1'] = engine.generate(start_symbol_name ="Get_Move1")
  d['wMove2'] = engine.generate(start_symbol_name ="Get_Move2")
  d['wMove3'] = engine.generate(start_symbol_name ="Get_MoveFin")
  d['w1'] = engine.generate(start_symbol_name ="Get_Wrestler1")
  d['w2'] = engine.generate(start_symbol_name ="Get_Wrestler2")
 







def return_engine():

  return GrammarEngine(file_path="grammars/c7.txt", initial_state = d) 



def grade():
    """The function James will be using to grade your component."""
    print("\n\n-- Component 6 -- ")
    component6()
