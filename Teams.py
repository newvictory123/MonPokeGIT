import enum
import discord
import random
import asyncio
from Match import match
from discord import app_commands
from discord.ext import commands
from MonPoke import MonPoke
from Moves import Moves

###moves
Tackle = Moves("Tackle", "Normal", "Physical", 40, 100)

###singular MonPokes
Zardichar = MonPoke("Zardichar", 108, "grass", 30, 78, 100, 100, 100, [Tackle])

ChuPika = MonPoke("ChuPika", 108, "fire", 30, 78, 100, 100, 100, [Tackle])

LetDig = MonPoke("LetDig", 108, "ground", 30, 78, 100, 100, 100, [Tackle])

SaurVenu = MonPoke.MonPoke("SaurVenu", 108, "Grass", 30, 78, 100, 100, 100, [Tackle])

Ianpers = MonPoke.MonPoke("Ianpers", 108, "Normal", 30, 78, 100, 100, 100, [Tackle])

ZoneMagne = MonPoke.MonPoke("Zonemagne", 108, "Steel", 30, 78, 100, 100, 100, [Tackle])

Ableclef = MonPoke.MonPoke("Ableclef", 108, "Fairy", 30, 78, 100, 100, 100, [Tackle])

RiAlta = MonPoke.MonPoke("Rialta", 108, "Dragon", 30, 78, 100, 100, 100, [Tackle])

LixTeel = MonPoke.MonPoke("Lixteel", 108, "Steel", 30, 78, 100, 100, 100, [Tackle])

###Premade teams
team1 = (LetDig, ChuPika, Zardichar)
team2 = (SaurVenu, Ianpers, ZoneMagne)
team3 = (Ableclef, RiAlta, LixTeel)

class Team(enum.Enum):
        
            LetDig_ChuPika_Zardichar = team1
            SaurVenu_IanPers_ZoneMagne = team2
            AbleClef_RiAlta_LixTeel = team3