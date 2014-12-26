import Player

class Team:
    '''This is a Team'''
    team_counter = 0    # static member
    
    def __init__(self, i_name = "Team name"):
        self.name = i_name
        self.players = []
        Team.team_counter += 1
        
    def addPlayer(self, p):
        #ToDo: Ueberpruefen ob der Spieler schon in der Mannschaft
        self.players.append(p)

    def print(self):
        print('Team', self.name, 'hat', len(self.players), 'Spieler:')
        for x in self.players:
            #print (x.name)
            x.print()
        
