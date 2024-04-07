import random

class MonPoke:
    def __init__(self, Name, HP, Type, Speed, Attack, Defense, SpAtk, SpDef):
        self.Name = Name
        self.HP = HP
        self.Type = Type
        self.Speed = Speed
        self.Attack = Attack
        self.Defense = Defense
        self.SpAtk = SpAtk
        self.SpDef = SpDef
        self.moves = []



def HP(H, L, EV, IV):
    finalHP= ((((2 * H + IV + (EV/4))*L)/100)+10+L)
    print(finalHP)

def Otherstat(B, IV, EV, L):
    finalstat = (((((2*B) + IV +(EV/4))*L)/100)+5)
    print(finalstat)

HP(108, 50, 74, random.randint(1,31))

Otherstat(130, random.randint(1,31), 190, 50)