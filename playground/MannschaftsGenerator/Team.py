import Player

class Team:
    '''This is a Team'''
    players = []
    def __init__(self, i_name = "Team name"):
        self.name = i_name
                
    def addPlayer(self, p): # = Player("Player made by the Team class")):
        players.append(p)

    def print(self):
        print('Team', self.name, 'hat', len(players), 'Spieler:')
        for x in players:
            print (x)
        
