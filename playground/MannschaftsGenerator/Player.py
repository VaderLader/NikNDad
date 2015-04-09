class Player:
    """Class for Players
    
       Usage: Player({'name': 'Vorname Name',
                      'attackpoints': 0,
                      'defencepoints': 0, 
                      'keeperpoint': 0})
    """
    player_counter = 0  #: static member
    weight_attack = 3 #: Gewichtung
    weight_defence = 2
    weight_keeper = 1    
    
    #: Mal sehen wo dieser Kommentar steht
    def __init__(self, d={'name': 'Vorname Name',
                            'attackpoints': 0,
                            'defencepoints': 0, 
                            'keeperpoints': 0}):
                            
    
        self.name = d['name']
        self.attackpoints = d['attackpoints']
        self.defencepoints = d['defencepoints']
        self.keeperpoints = d['keeperpoints']
        self.calcPlayerpoints()
        Player.player_counter += 1


    def print(self):
        print("--",  "Spieler:", self.name, "--",
              "\n| Angriff:", self.attackpoints,
              "\n| Verteidigung:", self.defencepoints,
              "\n| Torwart:", self.keeperpoints,
              "\n| Gesamt Punkte:", self.playerpoints, "\n---------------"
              )
              
    def calcPlayerpoints(self):
        """
        Die playerpoints werden als gewichtete Summe der Angriffs-, Abwehr-,
        und Torwart-Punkte berechnet.
        """
        self.playerpoints = (self.attackpoints * Player.weight_attack + \
                            self.defencepoints * Player.weight_defence + \
                            self.keeperpoints * Player.weight_keeper ) \
                            /(Player.weight_attack + Player.weight_defence \
                            + Player.weight_keeper)