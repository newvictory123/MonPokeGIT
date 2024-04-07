import MonPoke

class (MonPoke):
    def __init__(self,Name, Type, Speed, Attack, Defense, SpAtk, SpDef):
        self.Name = Name
        self.Type = Type
        self.Speed = Speed
        self.Attack = Attack
        self.Defense = Defense
        self.SpAtk = SpAtk
        self.SpDef = SpDef
        super().__init__(Name, Type, Speed, Attack, Defense, SpAtk, SpDef)


    def 