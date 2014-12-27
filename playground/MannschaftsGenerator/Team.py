import Player

class Team:
    '''This is a Team'''
    team_counter = 0    # static member
    
    def __init__(self, i_name = "Team name"):
        self.name = i_name
        self.players = []
        Team.team_counter += 1
        self.attackpoints = 0
        self.keeperpoints = 0
        self.defencepoints = 0
        
    def addPlayer(self, p):
        #ToDo: Ueberpruefen ob der Spieler schon in der Mannschaft
        self.players.append(p)
        self.attackpoints += p.attackpoints
        self.keeperpoints += p.keeperpoints
        self.defencepoints += p.defencepoints

    def removePlayer(self, p):
        self.players.pop(p)

    def print(self):
        print('Team', self.name, 'hat', len(self.players), 'Spieler:')
        for index, element in enumerate(self.players):
            print ('{} {}'.format(index, element.name))
            #x.print()
        print('Die Angriffstärke liegt bei', self.attackpoints)
        print('Die Abwehrstärke liegt bei', self.defencepoints)
        print('Die Torwartstärke liegt be liegt bei', self.keeperpoints)
Player.addPlayer('Hallo')
Player.addPlayer('Hi')
Player.addPlayer('Ho')
Player.removePlayer('Hi')
