import random
typematchups = {
    "Fire": {"Weaknesses": ["Rock", "Ground", "Water"], "Resistances": ["Bug", "Steel", "Fire", "Grass", "Ice", "Fairy"], "Immunities": []},
    "Water": {"Weaknesses": ["Grass", "Electric"], "Resistances": ["Water", "Fire", "Ice", "Steel"], "Immunities": []},
    "Grass": {"Weaknesses": ["Fire", "Bug", "Ice", "Poison", "Flying"], "Resistances": ["Water", "Grass", "Ground", "Electric"], "Immunities": []},
    "Electric": {"Weaknesses": ["Ground"], "Resistances": ["Electric", "Flying", "Steel"], "Immunities": []},
    "Bug": {"Weaknesses": ["Rock", "Flying", "Fire"], "Resistances": ["Fighting", "Ground", "Grass"], "Immunities": []},
    "Ground": {"Weaknesses": ["Grass", "Water", "Ice"], "Resistances": ["Poison", "Rock"], "Immunities": ["Electric"]},
    "Rock": {"Weaknesses": ["Fighting", "Ground", "Grass", "Water", "Steel"], "Resistances": ["Ice", "Flying", "Fire", "Poison"], "Immunities": []},
    "Steel": {"Weaknesses": ["Ground", "Fire", "Fighting"], "Resistances": ["Normal", "Flying", "Bug", "Rock", "Steel", "Grass", "Psychic", "Ice", "Dragon", "Fairy"], "Immunities": ["Poison"]},
    "Ice": {"Weaknesses": ["Fire", "Steel", "Fighting", "Rock"], "Resistances": ["Ice"], "Immunities": []},
    "Dragon": {"Weaknesses": ["Dragon", "Fairy", "Ice"], "Resistances": ["Fire", "Water", "Grass", "Electric"], "Immunities": []},
    "Fairy": {"Weaknesses": ["Poison", "Steel"], "Resistances": ["Fighting", "Bug", "Dark"], "Immunities": ["Dragon"]},
    "Fighting": {"Weaknesses": ["Flying", "Psychic", "Fairy"], "Resistances": ["Rock", "Bug", "Dark"], "Immunities": []},
    "Normal": {"Weaknesses": ["Fighting"], "Resistances": [], "Immunities": ["Ghost"]},
    "Psychic": {"Weaknesses": ["Bug", "Dark", "Ghost"], "Resistances": ["Fighting", "Psychic"], "Immunities": []},
    "Poison": {"Weaknesses": ["Gound", "Psychic"], "Resistances": ["Fighting", "Poison", "Bug", "Grass", "Fairy"], "Immunities": []},
    "Dark": {"Weaknesses": ["Fighting", "Bug", "Fairy", ], "Resistances": ["Ghost", "Dark"], "Immunities": ["Psychic"]},
    "Ghost": {"Weaknesses": ["Ghost", "Dark"], "Resistances": ["Bug", "Poison", ], "Immunities": ["Normal", "Fighting"]},
    "Flying": {"Weaknesses": ["Rock", "Electric", "Ice"], "Resistances": ["Fighting", "Bug", "Grass"], "Immunities": ["Ground"]}
    }

class Moves():
    def __init__(self, Name, Type, Sort, Power, Accuracy):
        self.Name = Name
        self.Type = Type
        self.Sort = Sort
        self.Power = Power
        self.Accuracy = Accuracy

    def damage(self, user, target):
        if random.randint(1, 100) > self.Accuracy:
            return 0
        if self.Sort == "Physical":
            Attack = user.Attack
            Defense = target.Defense
        elif self.Sort == "Special":
            Attack = user.SpAtk
            Defense = target.SpDef
        if random.randint(1, 16) == 16:
            Crit = 1.5
        else:
            Crit = 1
        if self.Type == user.Type:
            Stab = 1.5
        else:
            Stab = 1
        if self.Type in typematchups[str(target.Type)]["Weaknesses"]:
           Effectiveness = 2
        elif self.Type in typematchups[str(target.Type)]["Resistances"]:
            Effectiveness = 0.5
        elif self.Type in typematchups[str(target.Type)]["Immunities"]:
            Effectiveness = 0
        else:
            Effectiveness = 1
        damage = ((((2 * user.Level) / 5 + 2) * self.Power * (Attack / Defense)) / 50 + 2) * Crit * (random.randint(85, 100) / 100) * Stab * Effectiveness
        return damage