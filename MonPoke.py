import random
from Moves import Moves

class MonPoke:
    def __init__(self, Name, HP, Type, Speed, Attack, Defense, SpAtk, SpDef, level=50):
        self.Name = Name #str
        self.HP = HP #int
        self.Type = Type #tuple
        self.Speed = Speed #int
        self.Attack = Attack #int
        self.Defense = Defense #int
        self.SpAtk = SpAtk #int
        self.SpDef = SpDef #int
        self.moves = [] #list
        self.level = level #int



    def Health(self, EV):
        finalHP= ((((2 * self.HP + random.randint(1,31) + (EV/4))*50)/100)+10+50)
        print(finalHP)

    def Otherstat(B, IV, EV, L):
        finalstat = (((((2*B) + IV +(EV/4))*L)/100)+5)
        print(finalstat)

"""HP(108, 50, 74, random.randint(1,31))"""

"""Otherstat(130, random.randint(1,31), 190, 50)"""