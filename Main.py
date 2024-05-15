import discord
import random
import asyncio
import uuid
from Match import match
from Match import Player
from discord import app_commands
from discord.ext import commands
import Teams
import copy

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
            if channel in matches.keys() and matches[channel].IsJoinable(user.name, matches):
                player = Player(user.name)
                matches[channel].players.append(player)
                matches[channel].playernames.append(user.name)
                await interaction.response.send_message(f"{user} has joined {channel.name}!")
                print ("lijk")
            elif channel not in matches.keys():
                player = Player(user.name)
                newmatch = match(channel)
                newmatch.players.append(player)
                newmatch.playernames.append(user.name)
                matches[newmatch.channel] = newmatch
                await interaction.response.send_message(f"{user} has startes match in {channel.name} use /matchmake to join the match!")
                print("lidjf")
            else:
                await interaction.response.send_message("channel is occupied or user already in channel")    
    else:
       await interaction.response.send_message("Cant use this command in non-MonPoke Stadium channels")

@bot.tree.command(name = "quit")
async def quit(interaction: discord.integrations):
    channel = interaction.channel
    user = interaction.user
    
    if channel in matches.keys():
        for player in matches[channel].players:
            if player.playername == user.name:
                playerquit = player
        if matches[channel].IsQuitable(user.name):
            matches[channel].players.remove(playerquit)
            matches[channel].playernames.remove(user.name)
            del matches[channel]
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
    for player in matches[channel].players:
        if player == userchoosing:
            playerchoosing = player
    for teams in Teams.TeamDict.keys():
        if teams == team.value:
            playerchoosing.MonPokes = copy.deepcopy(Teams.TeamDict[teams])
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
async def chooseattack(interaction: discord.interactions, monpoke :str):
    user = interaction.user
    channel=interaction.channel
    for player in matches[channel].players:
        if player.playername == user.name:
            userchoosing = player
    for player in matches[channel].players:
        if player == userchoosing:
            playerchoosing = player
    if channel in matches.keys():
        if matches[channel].state == 1 or matches[channel].state == 2: 
            if user.name in matches[channel].playernames:
                for monpokes in playerchoosing.MonPokes:
                    if monpokes.Name == monpoke and playerchoosing.CanSwitch:
                        playerchoosing.CurrentMonPoke = monpokes
                        playerchoosing.HasAnswered = True
                        await interaction.response.send_message(f"you have chosen {playerchoosing.CurrentMonPoke.Name}", ephemeral = True)
                if playerchoosing.HasAnswered != True:
                    await interaction.response.send_message(f"{monpoke} not in team list or not able to switch", ephemeral = True)


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