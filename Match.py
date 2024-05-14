import discord
from discord import app_commands
from discord.ext import commands
import asyncio
import random
import Teams

states = [1,2]

class match():
    def __init__(self, channel):
        self.channel = channel
        self.players = []
        self.state = 0 
        self.states = [1,2]
        self.moveinturn = []
        self.gameover = False

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
                player.MonPokes = random.choice(list(Teams.TeamDict.values()))
                print(player.MonPokes)
                player.HasAnswered = False
            elif player.HasAnswered == True:
                player.HasAnswered = False
            print(player.MonPokes)
            

    async def Switch(self):
        await asyncio.sleep(2)
        for player in self.players:
            if player.HasAnswered == False and player.CanSwitch == True:
                for monpoke in player.MonPokes:
                    if monpoke.dead == False:
                        player.CurrentMonPoke = monpoke
                        player.CanSwitch = False
            elif player.HasAnswered == True:
                player.HasAnwered = False
                player.CanSwitch = False
            print(player.playername + "chosen" + player.CurrentMonPoke.Name)


        
    async def Turnsystem(self):
        await self.channel.send("Choose a move with '/chooseattack'")
        await self.channel.send("Or switch pokemon with '/switch'")
        await asyncio.sleep(30) 
        player1 = self.players[0]
        player2 = self.players[1]
        player1monpoke = player1.CurrentMonPoke
        print(player1monpoke)
        player2monpoke = player2.CurrentMonPoke
        print(player2monpoke)
        if player1.HasAnswered == True and player2.HasAnswered == True:
                    if player1monpoke.Speed > player2monpoke.Speed:
                        self.moveinturn.append(player1)
                        self.moveinturn.append(player2)
                    elif player1monpoke.Speed == player2monpoke.Speed:
                        movesinscene = [player1, player2]
                        randommove = random.choice(movesinscene)
                        if randommove == player1:
                            self.moveinturn.append(player1)
                            self.moveinturn.append(player2)
                        else: 
                            self.moveinturn.append(player2)
                            self.moveinturn.append(player1)      
                    else:
                        self.moveinturn.append(player2)
                        self.moveinturn.append(player1)
                    print(self.moveinturn)
                    for move in self.moveinturn:
                        if move == player1:
                            user = player1monpoke
                            userplayer = player1
                            target = player2.CurrentMonPoke
                            targetplayer = player2
                        else:
                            user = player2monpoke
                            userplayer = player2
                            target = player1.CurrentMonPoke
                            targetplayer = player1
                        if userplayer.chosenmove != None:
                                target.HP -= move.damage(user, target)
                                await self.channel.send(f"{user.Name} used {move.Name}")
                                await self.channel.send(f"{target.Name} takes {move.damage(user, target)} amount damage")
                                await self.channel.send(f"{target.Name} HP {target.HP} amount damage")
                        if target.HP <= 0:
                                target.dead = True
                        if target.dead == True and targetplayer.MonPokes != []:
                                await self.channel.send(f"{targetplayer} switch pokemon with switch function")
                                targetplayer.CanSwitch = True
                                targetplayer.MonPokes.remove(target)
                                print("dead")
                                await self.Switch()    
                        elif target.dead == True and targetplayer.MonPokes == []:
                                winner = user
                                self.gameover == True
                                print("dead game over")
                    if self.gameover == False:        
                        await self.Turnsystem()
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
        self.chosenmove = None
        self.MonPokes = None
        self.CurrentMonPoke = None
        self.HasAnswered = False
        self.CanSwitch = True
        