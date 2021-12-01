import location as loc
from rule_system.engine import RuleEngine



class hero:
  rule_engine = RuleEngine
  locz = loc
  def __init__(self, file, locationz):
    self.rule_engine = file
    self.locz = locationz


  def equip(self, weapon):
    if (self.in_inventory(weapon)):
      self.update_equip(weapon)
    else:
      print("illegal move, please try again")

  def run(self,location):
    self.check_moveable()
    holder = self.cur_location_node().run()
    holder2 = []
    for i in range(len(holder)):
      holder2.append(holder[i].name())
    if (location in holder2):
      self.update_location(location)
    else:
      print("illegal move, please try again")


  def map():
    pass

  def update_equip(self, newEquip):
    #updates it so the equip item is equip / stick is default
    oldItemLine = self.current_equip()
    if (oldItemLine != "Nah"):
      self.rule_engine.working_memory.delete_grounded_fact(oldItemLine)
    newItemLine = "Hero has equipped " + newEquip.title()
    self.rule_engine.working_memory.add_grounded_fact(newItemLine)

  def current_equip(self):
    items = ["knasty knife", "sparkling sword", "just javelin", "broad sword of judgement", "dusty darts", "stick"]

    for i in range (len(items)):
      itemLine = "Hero has equipped " + items[i].title()
      if (self.rule_engine.working_memory.has_fact(itemLine)):
          return itemLine
        
    return "Nah"
    

  def update_location(self,newLoc):
    #gets the location and then moves you
    oldItemLine = "Hero is at " + self.current_location().title()
    newItemLine = "Hero is at " + newLoc.title()
    self.rule_engine.working_memory.delete_grounded_fact(oldItemLine)
    self.rule_engine.working_memory.add_grounded_fact(newItemLine)
    
    #print(newItemLine)
    #print(self.rule_engine.working_memory.has_fact(oldItemLine))
    #print(self.rule_engine.working_memory.has_fact(newItemLine))
    
  
  def check_moveable(self):
    #checks to see if there are new unlocked areas and such
    for i in range (len(self.locz)):
      itemLine = self.locz[i].name().title() + " is not travelable"
      if (self.rule_engine.working_memory.has_fact(itemLine) and not self.locz[i].moveable()):
        self.locz[i].updateMoveable(True)



  def in_inventory(self,weapon):
    #checks whether or not the person has the weapon
    itemLine = "Hero has " + weapon.title()
    return self.rule_engine.working_memory.has_fact(itemLine)

  def check_inventory(self):
    #gives you which items you have
    inventory = []
    acceptable_items = ["knasty knife", "sparkling sword", "just javelin", "broad sword of judgement", "dusty darts", "stick"]
    print("you have:")
    for i in range (len(acceptable_items)):
      if(self.in_inventory(acceptable_items[i].title())):
        inventory.append(acceptable_items[i])
        print(acceptable_items[i])
    return inventory

  def current_location(self):
    #tells you where you currently are, or if you have somehow left the map

    places = ["brothel", "grass", "draw bridge", "sands", "ghost town", "poison fog", "library"]
    
    for i in range (len(places)):
      itemLine = "Hero is at " + places[i].title()
      if (self.rule_engine.working_memory.has_fact(itemLine)):
          return places[i]
        
    return "You have left the map"

  def update_maps():
    pass

  def check_equip(self):
    print (self.equip)

  def do_action(self,action):
    #adds in the action
    oldItemLine = "Hero is waiting"
    newItemLine = "Hero wants to " + action
    self.rule_engine.working_memory.add_grounded_fact(newItemLine)
    try: self.rule_engine.working_memory.delete_grounded_fact(oldItemLine)
    except:
      a = "b"
    
    #print(newItemLine)
    #print(self.rule_engine.working_memory.has_fact(oldItemLine))
    #print(self.rule_engine.working_memory.has_fact(newItemLine))


  def cur_location_node(self):
    #print(self.current_location())
    for i in range(len(self.locz)):
        #print(self.locz[i].name())
        if(self.locz[i].name() == self.current_location()):
          
          return self.locz[i]

      
    


