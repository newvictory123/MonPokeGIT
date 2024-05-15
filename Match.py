import discord
from discord import app_commands
from discord.ext import commands
import asyncio
import random
import Teams
import copy
states = [1,2]

class match():
    def __init__(self, channel):
        self.channel = channel
        self.players = []
        self.playernames = []
        self.state = 0 
        self.states = [1,2]
        self.moveinturn = []
        self.gameover = False

    def IsJoinable(self, player, matcheslist):
        print(self.players)
        if self.state == 0 and len(self.players) == 1 and self.channel in matcheslist.keys() and player not in self.playernames:
            return True
        
    def IsQuitable(self, player):
        if player in self.playernames and self.state == 0:
            return True 
    
    async def ChoosingTeam(self):
        await self.channel.send("Choose team with '/chooseteam'")
        await asyncio.sleep(15)
        for player in self.players:
            if player.HasAnswered == False:
                player.MonPokes = copy.deepcopy(random.choice(list(Teams.TeamDict.values())))
                print(player.MonPokes)
                player.HasAnswered = False
            elif player.HasAnswered == True:
                player.HasAnswered = False
            print(player.MonPokes)
            await self.channel.send(f"{player.playername} chose:")
            for monpokes in player.MonPokes:
                await self.channel.send(monpokes.Name)
            

    async def Switch(self):
        await self.channel.send("Choose starting monpoke with '/switch'")
        await asyncio.sleep(40)
        for player in self.players:
            if player.HasAnswered == False and player.CanSwitch == True:
                for monpoke in player.MonPokes:
                    print("Switch" + str(monpoke.Name))
                    player.CurrentMonPoke = monpoke
                    player.CanSwitch = False
                if self.state == 2:
                    await self.channel.send(f"{player.playername} switched to {player.CurrentMonPoke.Name}")
            elif player.HasAnswered == True:
                player.HasAnwered = False
                player.CanSwitch = False
        
            print(player.playername + "chosen" + player.CurrentMonPoke.Name)


        
    async def Turnsystem(self):
        player1 = self.players[0]
        player2 = self.players[1]
        player1.HasAnswered = False
        player2.HasAnswered = False
        player2.CanSwitch = True
        player1.CanSwitch = True
        self.moveinturn = []
        await self.channel.send("Choose a move with '/chooseattack'")
        await self.channel.send("Or switch monpoke with '/switch'")
        await asyncio.sleep(20) 
        player1monpoke = player1.CurrentMonPoke
        print(player1monpoke)
        player2monpoke = player2.CurrentMonPoke
        print(player2monpoke)
        if player1.HasAnswered == True and player2.HasAnswered == True:
                    player1.HasAnswered = False
                    player2.HasAnswered = False
                    player2.CanSwitch = False
                    player1.CanSwitch = False
                    if player1monpoke.Speed > player2monpoke.Speed:
                        self.moveinturn.append(player1)
                        self.moveinturn.append(player2)
                        player2.CanSwitch = False
                        player1.CanSwitch = False
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
                        if move.chosenmove != None:
                                target.HP -= move.chosenmove.damage(user, target)
                                await self.channel.send(f"{userplayer.playername}'s {user.Name} used {move.chosenmove.Name}")
                                await self.channel.send(f"{targetplayer.playername}'s {target.Name} takes {move.chosenmove.damage(user, target)} amount damage")
                                await self.channel.send(f"{targetplayer.playername}'s {target.Name} HP {target.HP} amount damage")
                                if target.HP <= 0:
                                        print(targetplayer.playername)
                                        print(target)
                                        if targetplayer.MonPokes != []:
                                            if len(targetplayer.MonPokes) == 1:
                                                winner = user
                                                self.gameover == True
                                                print("dead game over") 
                                                await self.channel.send(f"{winner} is the winner") 
                                            else:
                                                await self.channel.send(f"{targetplayer.playername} switch pokemon with switch function")
                                                targetplayer.CanSwitch = True
                                                targetplayer.MonPokes.remove(target)
                                                print("dead")
                                                print(targetplayer.MonPokes)
                                                await asyncio.sleep(1)
                                                await self.Switch()
                                                await asyncio.sleep(1)
                                                await self.Turnsystem()
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
        
    
class Player():
    def __init__(self, playername):
        self.playername = playername
        self.chosenmove = None
        self.MonPokes = None
        self.CurrentMonPoke = None
        self.HasAnswered = False
        self.CanSwitch = True