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
            player = Player(user.name)
            if channel in matches.keys() and matches[channel].IsJoinable(player, matches):
                matches[channel].players.append(player)
                await interaction.response.send_message(f"{user} has joined {channel.name}!")
                print ("lijk")
            else:
                newmatch = match(channel)
                newmatch.players.append(player)
                matches[newmatch.channel] = newmatch
                await interaction.response.send_message(f"{user} has startes match in {channel.name} use /matchmake to join the match!")
                print("lidjf")
    else:
       await interaction.response.send_message("Cant use this command in non-MonPoke Stadium channels")

@bot.tree.command(name = "quit")
async def quit(interaction: discord.integrations):
    channel = interaction.channel
    user = interaction.user
    for player in matches[channel].players:
        if player.playername == user.name:
            playerquit = player
    if channel in matches.keys() and matches[channel].IsQuitable(user):
        matches[channel].players.remove(playerquit)
        await interaction.response.send_message(f"{user} left {channel}")
    else:
        await interaction.response.send_message("Error")
            

@bot.tree.command(name = "chooseteam", description="team selected")
@app_commands.describe(team = "teams")
async def chooseteam(interaction: discord.Interaction, team: Teams.Team):
    user = interaction.user
    channel=interaction.channel
    for player in matches[channel].players:
        if player.playername == user.name:
            userchoosing = player
    playerchoosing = matches[channel].players[userchoosing]
    playerchoosing.MonPokes = team
    playerchoosing.HasAnswered = True

    await interaction.response.send_message(f'Your favourite team is {team.name}.')

@bot.tree.command(name = "chooseattack")
async def chooseattack(interaction: discord.interactions, attack: str):
    channel = interaction.channel
    user = interaction.user
    currentmatch = matches[channel]
    for player in currentmatch.players:
        if player.playername == user.name:
            currentplayer = player
    if channel in matches.keys() and currentmatch.state == 2 and currentplayer in currentmatch.players:
        if attack in player.CurrentMonPoke.moves.keys():
            currentplayer.chosenmove = player.CurrentMonPoke.moves[attack]
            currentplayer.HasAnswered = True
            await interaction.response.send_message(f"You have chosen {attack}", ephemeral = True)
        else:
            await interaction.response.send_message(f"{attack} not in pokemon move list", ephemeral = True)
    else:
        await interaction.response.send_message(f"error", ephemeral = True)
    None

@bot.tree.command(name = "switch")
async def chooseattack(interaction: discord.interactions):
    None


@bot.tree.command(name = "startgame")
async def startgame(interaction: discord.interactions):
    channel = interaction.channel
    user = interaction.user
    if len(matches[channel].players) == 2:
        matches[channel].state = 1
        await interaction.response.send_message(f"players: {matches[channel].players[0].playername + matches[channel].players[1].playername} started a match in {channel.name}")
        await matches[channel].GameLoop()
    else:
        await interaction.response.send_message("not enough players to start match")


token = get_token()
bot.run(token)