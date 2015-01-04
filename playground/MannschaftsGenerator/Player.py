class Player:
    '''Class for Players'''
    player_counter = 0  # static member
    weight_attack = 3
    weight_defence = 2
    weight_keeper = 1    
    
    
    def __init__(self, i_name = "Vorname Name", i_attackpoints = 0,
                 i_defencepoints = 0, i_keeperpoints = 0):
        self.name = i_name
        self.attackpoints = i_attackpoints
        self.defencepoints = i_defencepoints
        self.keeperpoints = i_keeperpoints
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
        self.playerpoints = (self.attackpoints * Player.weight_attack + \
                            self.defencepoints * Player.weight_defence + \
                            self.keeperpoints * Player.weight_keeper ) \
                            /(Player.weight_attack + Player.weight_defence \
                            + Player.weight_keeper)