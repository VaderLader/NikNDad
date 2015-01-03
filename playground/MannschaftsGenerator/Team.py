import Player

class Team:
    '''This is a Team'''
    team_counter = 0    # static member
    weight_attack = 3
    weight_defence = 2
    weight_keeper = 1

    def __init__(self, i_name = "Team name"):
        self.name = i_name
        self.players = []
        Team.team_counter += 1
        self.attackpoints = 0
        self.keeperpoints = 0
        self.defencepoints = 0

    def addPlayer(self, p):
        if p in self.players:
            print('Error:', p.name, 'ist schon in diesem Team!')
        else:
            self.players.append(p)
            self.calcTeampoints()
    
    def inputPlayer(self):
        name = input('Wie heißt der neue Spieler?\n')
        angriff = int(input('Wie gut ist er im Angriff?\n'))
        abwehr = int(input('Wie gut ist er in der Abwehr?\n'))
        tor = int(input('Wie gut ist er im Tor?\n'))
        p = Player.Player(name, angriff, abwehr, tor)
        p.print()
        return p


    def removeName(self, n):
        for index, element in enumerate(self.players):
            if element.name == n:
                self.players.pop(index)
                self.calcTeampoints()
                
                
    def removePlayer(self, p):
        for index, element in enumerate(self.players):
            if element == p:
                self.players.pop(index)
                self.calcTeampoints()
        # "list".index("element") returns the index of "element"
        # "list".pop("index") removes the element at "index"
        # ToDo: Check if p is part of the team before removing
        #self.players.pop( self.players.index(p) )

    def calcTeampoints(self):
        self.attackpoints = 0
        self.keeperpoints = 0
        self.defencepoints = 0
        for p in self.players:
            self.attackpoints += p.attackpoints
            self.keeperpoints += p.keeperpoints
            self.defencepoints += p.defencepoints
            self.teampoints = self.attackpoints * Team.weight_attack + self.defencepoints * Team.weight_defence + self.keeperpoints * Team.weight_keeper
        return self.teampoints

    def print(self):
        print('Team', self.name, 'hat', len(self.players), 'Spieler:')
        for index, element in enumerate(self.players):
            print ('{} {}'.format(index, element.name))
            #x.print()
        print('Die Angriffstärke liegt bei', self.attackpoints)
        print('Die Abwehrstärke liegt bei', self.defencepoints)
        print('Die Torwartstärke liegt be liegt bei', self.keeperpoints)
        print(self.players)

print('Hi')
