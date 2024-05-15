import enum
from Moves import Moves
from MonPoke import MonPoke

Tackle = Moves("Tackle", "Normal", "Physical", 40, 100)

ThrowerFlame = Moves("Thrower Flame", "Fire", "Special", 90, 100)

BoltThunder = Moves("Bolt Thunder", "Electric", "Special", 90, 100)

QuakeEarth = Moves("Quake Earth", "Ground", "Physical", 100, 100)

BallEnergy = Moves("Ball Energy", "Grass", "Special", 90, 100)

TacklePLUS = Moves("Tackle PLUS", "Normal", "Physical", 90, 100)

BallGyro = Moves("Ball Gyro", "Steel", "Special", 80, 100)

BlastMoon = Moves("Blast Moon", "Fairy", "Special", 95, 100)

ClawDragon = Moves("Claw Dragon", "Dragon", "Physical", 80, 100)

Frus = Moves("Frus", "Water", "Special", 90, 100) 

BirdBrave = Moves()

SlideRocks = Moves()

BreakBricks = Moves()

BallShadow = Moves()

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

LowSwell = MonPoke("LowSwell", 10, "Flying", 30, 78, 100, 100, 100, {"Tackle":Tackle})

EmGol = MonPoke("EmGol", 10, "Rock", 30, 78, 100, 100, 100, {"Tackle":Tackle})

ApePrime = MonPoke("ApePrime", 10, "Fighting", 30, 78, 100, 100, 100, {"Tackle":Tackle})

GarGen = MonPoke("GarGen", 10, "Ghost", 30, 78, 100, 100, 100, {"Tackle":Tackle})

PedeScoli = MonPoke ("PedeScoli", 10, "Poison", 30, 78, 100, 100, 100, {"Tackle":Tackle})

KazamAla = MonPoke("KazamAla", 10, "Psychic", 30, 78, 100, 100, 100, {"Tackle":Tackle})

LuggAva = MonPoke("LuggAva", 10, "Ice", 30, 78, 100, 100, 100, {"Tackle":Tackle})

SolAb = MonPoke("SolAb", 10, "Dark", 30, 78, 100, 100, 100, {"Tackle":Tackle})

VannyLea = MonPoke("VannyLea", 10, "Bug", 30, 78, 100, 100, 100, {"Tackle":Tackle})

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