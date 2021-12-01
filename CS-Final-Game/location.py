
class location:
  options =[]
  movez = []
  locName = ""
  isMoveable = False
  connectz = []

  def __init__(self,name,moveable,move):
    self.locName = name
    self.isMoveable = moveable
    self.movez = move
    self.options = ["help", "location", "moves", "run", "equip", "inventory"]
    self.connectz = []


  def connect(self,connections):
    self.connectz.append(connections)

  def updateMoveable(self,move):
  #updates if it is moveable
    self.isMoveable = move

  def moveable(self):
  #sees if the path is travelable
    return self.isMoveable

  def moves(self):
  #gives the users the move options for the room
    return self.movez

  def options(self):
    return self.options

  def name(self):
  #returns location
    return self.locName

  def run(self):
  #returns the spots you can move
    holder = []
    for i in range (len(self.connectz)):
      if (self.connectz[i].isMoveable):
        holder.append(self.connectz[i])
    return holder

  def connections(self):
    return self.connectz

  