import asyncio

class match():
    def __init__(self, channel, players, state):
        self.channel = channel
        self.players = players
        self.state = state 

    def IsJoinable(self, player, matcheslist):
        if self.state == 0 and len(self.players) == 1 and self.channel in matcheslist.keys() and matcheslist[self.channel].state == 0 and len(matcheslist[self.channel].players) == 1 and player not in matcheslist[self.channel].players:
            return True
        
    def IsQuitable(self, player):
        if player in self.players and self.state == 0:
            return True 
        
    def Turnsystem():
        """while true:
            if playeranswer == True and player2answer == True:
                if Player1.team[currentmonpoke].speed > Player2.team[currentmonpoke2].speed:
                    Moveinturn.append(chosenmove1)
                    Moveinturn.append(chosenmove2)
                elif Player1.team[currentmonpoke].speed == Player2.team[currentmonpoke2].speed:
                    randommove = choose.random(chosenmove1, chosenmove2)
                    if randommove == chosenmove1:
                        Moveinturn.append(chosenmove1)
                        Moveinturn.append(chosenmove2)
                    else: 
                        Moveinturn.append(chosenmove2)
                        Moveinturn.append(chosenmove1)      
                else:
                    Moveinturn.append(chosenmove2)
                    Moveinturn.append(chosenmove1)
                for move in moveinturn:
                    if move == chosenmove1
                        target = player2.team.currentmonpoke
                    else:
                        target = player1.team.currentmonpoke
                    move.attack(target)
                    if target.dead == true:
                        target.player.chancetoswitch = true
                    


                
                
        """
        
    
class Player():
    def __init__(self, playername):
        self.playername = playername
        self.MonPokes = []
        self.CurrentMonPoke = None
        