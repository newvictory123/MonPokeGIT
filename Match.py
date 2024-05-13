import discord
from discord import app_commands
from discord.ext import commands
import asyncio
import random
from Teams import Team

states = [1,2]

class match():
    def __init__(self, channel):
        self.channel = channel
        self.players = []
        self.state = 0 
        self.states = [1,2]
        self.moveinturn = []

    def IsJoinable(self, player, matcheslist):
        if self.state == 0 and len(self.players) == 1 and self.channel in matcheslist.keys() and player not in self.players:
            return True
        
    def IsQuitable(self, player):
        if player in self.players and self.state == 0:
            return True 
    
    async def ChoosingTeam(self):
        await asyncio.sleep(2)
        for player in self.players:
            if player.HasAnswered == False:
                player.MonPokes = random.choice(list(Team))
                player.HasAnswered = False
            elif player.HasAnswered == True:
                player.HasAnswered = False
            print(player.MonPokes)
            

    async def Switch(self):
        await asyncio.sleep(2)
        for player in self.players:
            if player.HasAnswered == False:
                player.CurrentMonPoke = player.MonPokes[random.randint(0,2)]
                player.HasAnswered = False
            if player.HasAnswered == True:
                player.HasAnwered = False


        
    async def Turnsystem(self):
        self.channel.send("Choose a move with '/chooseattack'")
        await asyncio.sleep(30) 
        player1 = self.players[0]
        player2 = self.players[1]
        if player1.HasAnswered == True and player2.HasAnswered == True:
                    if player1.team[player1.CurrentMonPoke].speed > player2.team[player2.CurrentMonPoke].speed:
                        self.moveinturn.append(player1.chosenmove)
                        self.moveinturn.append(player2.chosenmove)
                    elif player1.team[player1.CurrentMonPoke].speed == player2.team[player2.CurrentMonPoke].speed:
                        movesinscene = (player1.chosenmove, player2.chosenmove)
                        randommove = random.choice(movesinscene)
                        if randommove == player1.chosenmove:
                            self.moveinturn.append(player1.chosenmove)
                            self.moveinturn.append(player2.chosenmove)
                        else: 
                            self.moveinturn.append(player2.chosenmove)
                            self.moveinturn.append(player1.chosenmove)      
                    else:
                        self.moveinturn.append(player2.chosenmove)
                        self.moveinturn.append(player1.chosenmove)
                    for move in self.moveinturn:
                        if move == player1.chosenmove:
                            target = player2.team.currentmonpoke
                            targetplayer = player2
                        else:
                            target = player1.team.currentmonpoke
                            targetplayer = player1
                        move.attack(target)
                        if target.dead == True and targetplayer.monpokes != []:
                            target.player.chancetoswitch = True 
                        elif target.dead == True and targetplayer.monpokes == []:
                            self.GameOver==True
                    if self.GameOver == True:
                        print ("gameover")
                    else:
                        if target.player.chancetoswitch == True: 
                            self.switch()
                        await self.TurnSystem()
        else: 
            await self.channel.send("Users didnt answer")
            await self.Turnsystem()
                      
    
    async def GameLoop(self):
        for states in self.states:
         if self.state == 1:
            await self.ChoosingTeam()
            await self.Switch()
            self.state = 2
            continue
         elif self.state == 2:
            await self.Turnsystem()
            self.state = 3
            continue
        
    
class Player():
    def __init__(self, playername):
        self.playername = playername
        self.MonPokes = None
        self.CurrentMonPoke = None
        self.HasAnswered = False
        