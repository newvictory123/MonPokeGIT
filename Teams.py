import enum
from Moves import Moves
from MonPoke import MonPoke

Tackle = Moves("Tackle", "Normal", "Physical", 40, 100)

ThrowerFlame = Moves("ThrowerFlame", "Fire", "Special", 90, 100)

BoltThunder = Moves("BoltThunder", "Electric", "Special", 90, 100)

QuakeEarth = Moves("QuakeEarth", "Ground", "Physical", 100, 100)

BallEnergy = Moves("BallEnergy", "Grass", "Special", 90, 100)

TacklePLUS = Moves("TacklePLUS", "Normal", "Physical", 90, 100)

BallGyro = Moves("BallGyro", "Steel", "Special", 80, 100)

BlastMoon = Moves("BlastMoon", "Fairy", "Special", 95, 100)

ClawDragon = Moves("ClawDragon", "Dragon", "Physical", 80, 100)

Frus = Moves("Frus", "Water", "Special", 90, 100) 

###singular MonPokes
Zardichar = MonPoke("Zardichar", 10, "Grass", 30, 78, 100, 100, 100,{"Tackle":Tackle})

ChuPika = MonPoke("ChuPika", 10, "Fire", 30, 78, 100, 100, 100,{"Tackle":Tackle})

LetDig = MonPoke("LetDig", 10, "Ground", 30, 78, 100, 100, 100,{"Tackle":Tackle})

SaurVenu = MonPoke("SaurVenu", 10, "Grass", 30, 78, 100, 100, 100, {"Tackle":Tackle})

Ianpers = MonPoke("Ianpers", 10, "Normal", 30, 78, 100, 100, 100, {"Tackle":Tackle})

ZoneMagne = MonPoke("Zonemagne", 10, "Steel", 30, 78, 100, 100, 100, {"Tackle":Tackle})

Ableclef = MonPoke("Ableclef", 10, "Fairy", 30, 78, 100, 100, 100, {"Tackle":Tackle})

OrusHax = MonPoke("OrusHax", 10, "Dragon", 30, 78, 100, 100, 100, {"Tackle":Tackle})

ToiseBlas = MonPoke("ToiseBlas", 10, "Water", 30, 78, 100, 100, 100, {"Tackle":Tackle})

###Premade teams
team1 = (LetDig, ChuPika, Zardichar)
team2 = (SaurVenu, Ianpers, ZoneMagne)
team3 = (Ableclef, OrusHax, ToiseBlas)

TeamDict = {team1 : [LetDig, ChuPika, Zardichar],
team2 : [SaurVenu, Ianpers, ZoneMagne],
team3 : [Ableclef, OrusHax, ToiseBlas]}

class Team(enum.Enum):
            LetDig_ChuPika_Zardichar = team1
            dlkj= team2
            ldkfj=team3