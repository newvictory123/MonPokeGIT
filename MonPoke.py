import random
from Moves import Moves

class MonPoke:
    def __init__(self, Name, HP, Type, Speed, Attack, Defense, SpAtk, SpDef, moves, level=50, dead = False):
        self.Name = Name
        self.HP = self.Health(HP)
        self.Type = Type
        self.level = level
        self.Speed = self.Otherstat(Speed)
        self.Attack = self.Otherstat(Attack)
        self.Defense = self.Otherstat(Defense)
        self.SpAtk = self.Otherstat(SpAtk)
        self.SpDef = self.Otherstat(SpDef)
        self.moves = moves
        self.dead = dead



    def Health(self, Base):
        finalHP= ((((2 * Base + random.randint(1,31) + (85/4))*50)/100)+10+50)
        return finalHP
        print(finalHP)

    def Otherstat(self, stat):
        finalstat = (((((2*stat) + random.randint(0, 31) +(85/4))*self.level)/100)+5)
        return finalstat
        print(finalstat)

