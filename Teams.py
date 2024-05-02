import enum
import discord
import random
import asyncio
from Match import match
from discord import app_commands
from discord.ext import commands
from MonPoke import MonPoke

###singular MonPokes
Zardichar = MonPoke("Zardichar", 108, "grass", 30, 78, 100, 100, 100)

ChuPika = MonPoke("ChuPika", 108, "fire", 30, 78, 100, 100, 100)

LetDig = MonPoke("LetDig", 108, "ground", 30, 78, 100, 100, 100, level = 40)

Saurvenu = MonPoke.MonPoke("SaurVenu", 108, "Grass", 30, 78, 100, 100, 100)

Ianpers = MonPoke.MonPoke("Ianpers", 108, "Normal", 30, 78, 100, 100, 100)

Zonemagne = MonPoke.MonPoke("Zonemagne", 108, "Steel", 30, 78, 100, 100, 100)

Ableclef = MonPoke.MonPoke("Ableclef", 108, "Fairy", 30, 78, 100, 100, 100)

Rialta = MonPoke.MonPoke("Rialta", 108, "Dragon", 30, 78, 100, 100, 100)

Lixteel = MonPoke.MonPoke("Lixteel", 108, "Steel", 30, 78, 100, 100, 100)

###Premade teams
team1 = (LetDig, ChuPika, Zardichar)
team2 = (Saurvenu, Ianpers, Zonemagne)
team3 = (Ableclef, Rialta, Lixteel)

class Team(enum.Enum):
        
            LetDig_ChuPika_Zardichar = team1
            banana = 2
            cherry = 35