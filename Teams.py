import enum
from Moves import Moves
from MonPoke import MonPoke

Tackle = Moves("Tackle", "Normal", "Physical", 40, 100)

ThrowerFlame = Moves("Thrower Flame", "Fire", "Special", 90, 100)

BoltThunder = Moves("Bolt Thunder", "Electric", "Special", 90, 100)

QuakeEarth = Moves("QuakeEarth", "Ground", "Physical", 100, 100)

BallEnergy = Moves("Ball Energy", "Grass", "Special", 90, 100)

TacklePLUS = Moves("Tackle PLUS", "Normal", "Physical", 90, 100)

BallGyro = Moves("Ball Gyro", "Steel", "Special", 80, 100)

BlastMoon = Moves("Blast Moon", "Fairy", "Special", 95, 100)

ClawDragon = Moves("Claw Dragon", "Dragon", "Physical", 80, 100)

Frus = Moves("Frus", "Water", "Special", 90, 100) 

BirdBrave = Moves("Bird Brave", "Flying", "Physical", 100,100)

SlideRocks = Moves("Slide Rocks", "Rocks", "Physical", 80, 90)

BreakBricks = Moves("Break Bricks", "Fighting", "Physical", 80, 100)

BallShadow = Moves("Ball Shadow", "Ghost", "Special", 80, 100)

JabPoison = Moves("Jab Poison", "Poison", "Physical", 80, 100)

ChicPsy = Moves("ChicPsy", "Psychic", "Special", 90, 100)

CrashIcicle = Moves("Crash Icicle", "Ice", "Physical", 85, 90)

SlashNight = Moves("Slash Night", "Dark", "Physical", 80, 100)

ScissorX = Moves("Scissor X", "Bug", "Physical", 80, 100)

###singular MonPokes
Zardichar = MonPoke("Zardichar", 10, "Grass", 30, 78, 100, 100, 100,{"Tackle":Tackle, "ThrowerFlame": ThrowerFlame, "Break Bricks": BreakBricks, "Bird Brave": BirdBrave})

ChuPika = MonPoke("ChuPika", 10, "Fire", 30, 78, 100, 100, 100,{"Tackle":Tackle, "BoltThunder": BoltThunder, "Frus": Frus, "Ball Gyro": BallGyro})

LetDig = MonPoke("LetDig", 10, "Ground", 30, 78, 100, 100, 100,{"Tackle":Tackle, "QuakeEarth": QuakeEarth, "Slide Rocks": SlideRocks, "Tackle PLUS": TacklePLUS})

SaurVenu = MonPoke("SaurVenu", 10, "Grass", 30, 78, 100, 100, 100, {"Tackle":Tackle, "Ball Energy": BallEnergy, "Jab Poison": JabPoison, "QuakeEarth": QuakeEarth})

Ianpers = MonPoke("Ianpers", 10, "Normal", 30, 78, 100, 100, 100, {"Tackle":Tackle, "Tackle PLUS": TacklePLUS, "Claw Dragon": ClawDragon, "Crash Icicle": CrashIcicle})

ZoneMagne = MonPoke("Zonemagne", 10, "Steel", 30, 78, 100, 100, 100, {"Tackle":Tackle, "Ball Gyro": BallGyro, "BoltThunder": BoltThunder, "ChicPsy": ChicPsy})

Ableclef = MonPoke("Ableclef", 10, "Fairy", 30, 78, 100, 100, 100, {"Tackle":Tackle, "Blast Moon": BlastMoon, "ChicPsy": ChicPsy, "Ball Energy": BallEnergy})

OrusHax = MonPoke("OrusHax", 10, "Dragon", 30, 78, 100, 100, 100, {"Tackle":Tackle, "Claw Dragon": ClawDragon, "QuakeEarth": QuakeEarth, "Slash Night": SlashNight})

ToiseBlas = MonPoke("ToiseBlas", 10, "Water", 30, 78, 100, 100, 100, {"Tackle":Tackle, "Frus": Frus, "Ball Gyro": BallGyro, "Tackle PLUS": TacklePLUS})

LowSwell = MonPoke("LowSwell", 10, "Flying", 30, 78, 100, 100, 100, {"Tackle":Tackle, "Bird Brave": BirdBrave, "Scissor X": ScissorX, "Break Bricks": BreakBricks})

EmGol = MonPoke("EmGol", 10, "Rock", 30, 78, 100, 100, 100, {"Tackle":Tackle, "Slide Rocks": SlideRocks, "QuakeEarth": QuakeEarth, "Ball Gyro": BallGyro})

ApePrime = MonPoke("ApePrime", 10, "Fighting", 30, 78, 100, 100, 100, {"Tackle":Tackle, "Break Bricks": BreakBricks, "Slash Night": SlashNight, "Jab Poison": JabPoison})

GarGen = MonPoke("GarGen", 10, "Ghost", 30, 78, 100, 100, 100, {"Tackle":Tackle, "Ball Shadow": BallShadow, "Jab Poison": JabPoison, "ChicPsy": ChicPsy})

PedeScoli = MonPoke ("PedeScoli", 10, "Poison", 30, 78, 100, 100, 100, {"Tackle":Tackle, "Jab Poison": JabPoison, "Scissor X": ScissorX, "Slash Night": SlashNight})

KazamAla = MonPoke("KazamAla", 10, "Psychic", 30, 78, 100, 100, 100, {"Tackle":Tackle, "ChicPsy": ChicPsy, "Ball Shadow": BallShadow, "Bolt Thunder": BoltThunder})

LuggAva = MonPoke("LuggAva", 10, "Ice", 30, 78, 100, 100, 100, {"Tackle":Tackle, "Crash Icicle": CrashIcicle, "Slide Rocks": SlideRocks, "Frus": Frus})

SolAb = MonPoke("SolAb", 10, "Dark", 30, 78, 100, 100, 100, {"Tackle":Tackle, "Slash Night": SlashNight, "Claw Dragon": ClawDragon, "ThrowerFlame": ThrowerFlame})

VannyLea = MonPoke("VannyLea", 10, "Bug", 30, 78, 100, 100, 100, {"Tackle":Tackle, "Scissor X": ScissorX, "Ball Energy": BallEnergy, "Slash Night": SlashNight})

###Premade teams
team1 = (LetDig, ChuPika, Zardichar)
team2 = (SaurVenu, Ianpers, ZoneMagne)
team3 = (Ableclef, OrusHax, ToiseBlas)
team4 = (LowSwell, EmGol, ApePrime)
team5 = (GarGen, PedeScoli, KazamAla)
team6 = (LuggAva, SolAb, VannyLea)

TeamDict = {
team1: [LetDig, ChuPika, Zardichar],
team2: [SaurVenu, Ianpers, ZoneMagne],
team3: [Ableclef, OrusHax, ToiseBlas],
team4: [LowSwell, EmGol, ApePrime], 
team5: [GarGen, PedeScoli, KazamAla], 
team6: [LuggAva, SolAb, VannyLea]
}

class Team(enum.Enum):
            LetDig_ChuPika_Zardichar = team1
            dlkj= team2
            ldkfj=team3