import Player

class Team:
    """Class for Team
        Usage: Team({'name': 'Team name', 
                            'players': []
                            })
    
    
    """
    team_counter = 0    # static member
    weight_attack = 3
    weight_defence = 2
    weight_keeper = 1

    def __init__(self, d = {'name': 'Team name', 
                            'players': []
                            }):
        self.name = d['name']
        self.players = d['players']
        Team.team_counter += 1
        self.attackpoints = 0
        self.keeperpoints = 0
        self.defencepoints = 0
        # Calculate all points of the team        
        self.teampoints = self.calcTeampoints()
                
        self.Mitglieder = "Mitglieder"
        #self.teampoints = d['teampoints']

    def addPlayer(self, p):
        if p in self.players:
            print('Error:', p.name, 'ist schon in diesem Team!')
        else:
            self.players.append(p)
            self.calcTeampoints()

    def inputPlayer(self):
        """
        Nicht benutzt
        :returns: The newly input player.
        :rtype: Player.
        """
        
        name = input('Wie heißt der neue Spieler?\n')
        angriff = int(input('Wie gut ist er im Angriff?\n'))
        abwehr = int(input('Wie gut ist er in der Abwehr?\n'))
        tor = int(input('Wie gut ist er im Tor?\n'))
        p = Player.Player({'name': name,
                            'attackpoints': angriff,
                            'defencepoints': abwehr, 
                            'keeperpoint': tor})
        p.print()
        return p


    def removeName(self, name):
        """Removes a Player by it's Name

        :param name: Name
        :type name: str 
        :returns: -
        :rtype: -
        """
    
        for index, element in enumerate(self.players):
            if element.name == name:
                self.players.pop(index)
                self.calcTeampoints()
                
    def removeByIndex(self, index):
        """Removes a Player by it's index 

        :param index: index is the position in the Team's players list.
        :type index: int. 
        :returns: The removed Player is returned.
        :rtype: Player.
        """        
        p = self.players.pop(index)
        self.calcTeampoints()
        return p 
                
    def removePlayer(self, p):
        for index, element in enumerate(self.players):
            if element == p:
                self.players.pop(index)
                self.calcTeampoints()
                
        # "list".index("element") returns the index of "element"
        # "list".pop("index") removes the element at "index"
        # ToDo: Check if p is part of the team before removing
        #self.players.pop( self.players.index(p) )
        
    def removeAllPlayers(self):
        self.players = []            
        self.calcTeampoints()
            
    def calcTeampoints(self):
        #: Calculate all points from scratch
        self.attackpoints = 0
        self.keeperpoints = 0
        self.defencepoints = 0
        self.teampoints = 0
        for p in self.players:
            self.attackpoints += p.attackpoints
            self.keeperpoints += p.keeperpoints
            self.defencepoints += p.defencepoints
        
        self.teampoints = (self.attackpoints * Team.weight_attack + \
                    self.defencepoints * Team.weight_defence + \
                    self.keeperpoints * Team.weight_keeper)/ \
                    (Team.weight_attack+Team.weight_defence+Team.weight_keeper)
                            
        return self.teampoints

    def print(self):
        Mitglieder = 'Team ' + self.name + ' hat'+ str(len(self.players)) + ' Spieler:\n'
        for index, element in enumerate(self.players):
            Mitglieder += ('{} {}'.format(index, element.name) +'\n')
        Mitglieder += 'Die Angriffstärke liegt bei: '+ str(self.attackpoints) + '\n'
        Mitglieder += 'Die Abwehrstärke liegt bei: '+ str(self.defencepoints) + '\n'
        Mitglieder += 'Die Torwartstärke liegt liegt bei: ' + str(self.keeperpoints) + '\n'
        Mitglieder += 'Gesamtstärke liegt bei: '+ str(self.teampoints) +'\n'
        #print(Mitglieder)
        return Mitglieder

    def shiftPlayersFromTeam(self, otherTeam):
        ''' Method to shift all players from otherTeam. The otherTeam has no players 
            afterwards '''   
        print('In shiftPlayersFromTeam','id(otherTeam)=', id(otherTeam), 'otherTeam.name=', otherTeam.name, ' len=', len(otherTeam.players))
        print('len(self.players)',len(self.players))
        self.players = self.players + otherTeam.players    
        print('len(self.players)',len(self.players))
        self.calcTeampoints()
        otherTeam.removeAllPlayers() 
    
    def shiftNPlayersFromTeam(self, otherTeam, n):
        ''' Method to shift the first n players from otherTeam. The otherTeam has no players 
            afterwards '''   
        print('In shiftNPlayersFromTeam','id(otherTeam)=', id(otherTeam),
              'otherTeam.name=', otherTeam.name, ' len=',
              len(otherTeam.players))
        print('len(self.players)',len(self.players))
        
        #for index, p in enumerate(otherTeam.players):
            
        #    if index < n :
        for index in range(0, n):
            self.addPlayer(otherTeam.players[index])
            print(index,n, len(self.players))
        #for index in range(0, n):
        #    otherTeam.removePlayer(otherTeam.players[index])
                  
        print("+++",index,n)
        print("vvvv")
        self.calcTeampoints()
        otherTeam.calcTeampoints()
        print('End of shiftNPlayersFromTeam')
        
