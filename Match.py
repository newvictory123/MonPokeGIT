class match():
    def __init__(self, channel, players, state):
        self.channel = channel
        self.players = players
        self.state = state 

    def IsJoinable(self, player, matcheslist):
        if self.state == 0 and len(self.players) == 1 and self.channel in matcheslist.keys() and matcheslist[self.channel].state == 0 and len(matcheslist[self.channel].players) == 1 and player not in matcheslist[self.channel].players:
            return True
        else:
            return False
        
    def IsQuitable(self, player):
        if player in self.players and self.state == 0:
            return True 
    
class Player():
    def __init__(self):
        self.MonPokes = []
        