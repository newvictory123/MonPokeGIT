import enum
from Moves import Moves
from MonPoke import MonPoke

Tackle = Moves("Tackle", "Normal", "Physical", 40, 100)

###singular MonPokes
Zardichar = MonPoke("Zardichar", 108, "grass", 30, 78, 100, 100, 100,{"Tackle":Tackle})

ChuPika = MonPoke("ChuPika", 108, "fire", 30, 78, 100, 100, 100,{"Tackle":Tackle})

LetDig = MonPoke("LetDig", 108, "ground", 30, 78, 100, 100, 100,{"Tackle":Tackle})

<<<<<<< Updated upstream
Saurvenu = MonPoke("SaurVenu", 108, "Grass", 30, 78, 100, 100, 100,{"Tackle":Tackle})

Ianpers = MonPoke("Ianpers", 108, "Normal", 30, 78, 100, 100, 100,{"Tackle":Tackle})

Zonemagne = MonPoke("Zonemagne", 108, "Steel", 30, 78, 100, 100, 100,{"Tackle":Tackle})

Ableclef = MonPoke("Ableclef", 108, "Fairy", 30, 78, 100, 100, 100,{"Tackle":Tackle})

Rialta = MonPoke("Rialta", 108, "Dragon", 30, 78, 100, 100, 100,{"Tackle":Tackle})

Lixteel = MonPoke("Lixteel", 108, "Steel", 30, 78, 100, 100, 100,{"Tackle":Tackle})

###Premade teams
team1 = [LetDig, ChuPika, Zardichar]
team2 = [Saurvenu, Ianpers, Zonemagne]
team3 = [Ableclef, Rialta, Lixteel]
=======
SaurVenu = MonPoke("SaurVenu", 108, "Grass", 30, 78, 100, 100, 100, [Tackle])

Ianpers = MonPoke("Ianpers", 108, "Normal", 30, 78, 100, 100, 100, [Tackle])

ZoneMagne = MonPoke("Zonemagne", 108, "Steel", 30, 78, 100, 100, 100, [Tackle])

Ableclef = MonPoke("Ableclef", 108, "Fairy", 30, 78, 100, 100, 100, [Tackle])

RiaAlta = MonPoke("Rialta", 108, "Dragon", 30, 78, 100, 100, 100, [Tackle])

LixTeel = MonPoke("Lixteel", 108, "Steel", 30, 78, 100, 100, 100, [Tackle])

###Premade teams
team1 = (LetDig, ChuPika, Zardichar)
team2 = (SaurVenu, Ianpers, ZoneMagne)
team3 = (Ableclef, RiaAlta, LixTeel)
>>>>>>> Stashed changes

class Team(enum.Enum):
            LetDig_ChuPika_Zardichar = team1
            dlkj= team2
            ldkfj=team3