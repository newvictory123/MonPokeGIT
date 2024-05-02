import asyncio
import random

class match():
    def __init__(self, channel, players, state, moveinturn):
        self.channel = channel
        self.players = players
        self.state = state 
        self.moveinturn = moveinturn

    def IsJoinable(self, player, matcheslist):
        if self.state == 0 and len(self.players) == 1 and self.channel in matcheslist.keys() and matcheslist[self.channel].state == 0 and len(matcheslist[self.channel].players) == 1 and player not in matcheslist[self.channel].players:
            return True
        
    def IsQuitable(self, player):
        if player in self.players and self.state == 0:
            return True 
        
    def Turnsystem(self):
        player1 = self.players[0]
        player2 = self.players[1]
        while True:
            for player in self.players:
                if len(player.MonPokes) == []:
                    break
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
                        else:
                            target = player1.team.currentmonpoke
                        move.attack(target)
                        if target.dead == True:
                            target.player.chancetoswitch = True 
                    if target.player.chancetoswitch == True: 
                        self.switch()
                    break   
    
    async def GameLoop(self, quitentered, gamestate, states):
        for states in states:
         if quitentered.value == 1:
            break
         elif gamestate.value == 1:
            await self.Choosingteam()
            gamestate.value = 2
            continue
         elif gamestate.value == 2:
            await self.Turnsystem()
            gamestate.value = 3
            continue
        
    
class Player():
    def __init__(self, playername, MonPokes, CurrentMonPoke, HasAnswered):
        self.playername = playername
        self.MonPokes = MonPokes
        self.CurrentMonPoke = CurrentMonPoke
        self.HasAnswered = HasAnswered
        