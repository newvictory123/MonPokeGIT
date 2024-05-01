import discord
import random
import asyncio
import uuid
from Match import match
from Match import Player
from discord import app_commands
from discord.ext import commands
import Teams

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

TOK_FILE = "Token.txt"

matches = {}

def get_token():
    tokfile = open(TOK_FILE,"r")
    token = tokfile.read()
    tokfile.close()
    return token

@bot.event
async def on_ready():
    print("connected")
    try:
        synced = await bot.tree.sync()
        print(f"{len (synced)} commmands")
    except Exception as v:
        print(v)

@bot.tree.command(name = "matchmake")
async def matchmake(interaction: discord.interactions):
    channel = interaction.channel
    user = interaction.user
    print(matches.keys())
    if channel.name[:15] == "monpoke-stadium":
            if channel in matches.keys() and matches[channel].IsJoinable(user, matches):
                matches[channel].players.append(user)
                await interaction.response.send_message(f"{user} has joined {channel.name}!")
                print ("lijk")
            else:
                newmatch = match( channel, [], 0)
                newmatch.players.append(user)
                matches[newmatch.channel] = newmatch
                await interaction.response.send_message(f"{user} has startes match in {channel.name} use /matchmake to join the match!")
                print("lidjf")
    else:
       await interaction.response.send_message("Cant use this command in non-MonPoke Stadium channels")

@bot.tree.command(name = "quit")
async def quit(interaction: discord.integrations):
    channel = interaction.channel
    user = interaction.user
    if channel in matches.keys() and matches[channel].IsQuitable(user):
        matches[channel].players.remove(user)
        await interaction.response.send_message(f"{user} left {channel}")
    else:
        await interaction.response.send_message("Error")
            

@bot.tree.command(name = "chooseteam", description="team selected")
@app_commands.describe(team = "teams")
async def chooseteam(interaction: discord.Interaction, team: Teams.Team):
    await interaction.response.send_message(f'Your favourite team is {team.name}.')

@bot.tree.command(name = "chooseattack")
async def chooseattack(interaction: discord.interactions, atk1: str, atk2: str, atk3: str, atk4: str):
    None

@bot.tree.command(name = "startgame")
async def startgame(interaction: discord.interactions):
    channel = interaction.channel
    user = interaction.user
    if len(matches[channel].players) == 2:
        for player in matches[channel].players:
            Player(player)
    else:
        await interaction.response.send_message("not enough players to start match")


token = get_token()
bot.run(token)