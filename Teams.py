import enum
import discord
import random
import asyncio
from Match import match
from discord import app_commands
from discord.ext import commands
import MonPoke
import MonPokeTeams

###singular MonPokes
Zardichar = MonPoke.MonPoke("Zardichar", 108, "grass", 30, 78, 100, 100, 100)

ChuPika = MonPoke.MonPoke("ChuPika", 108, "fire", 30, 78, 100, 100, 100)

LetDig = MonPoke.MonPoke("LetDig", 108, "ground", 30, 78, 100, 100, 100)

###Premade teams
team1 = (LetDig, ChuPika, Zardichar)

class Team(enum.Enum):
            LetDig_ChuPika_Zardichar = team1
            banana = 2
            cherry = 3