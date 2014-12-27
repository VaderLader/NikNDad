class Player:
    '''Class for Players'''
    player_counter = 0  # static member
    
    def __init__(self, i_name = "Vorname Name", i_attackpoints = 0, i_defencepoints = 0, i_keeperpoints = 0):
        self.name = i_name
        self.attackpoints = i_attackpoints
        self.defencepoints = i_defencepoints
        self.keeperpoints = i_keeperpoints
        Player.player_counter += 1
        
    def print(self):
        print("--",  "Spieler:", self.name, "--",
              "\n| Angriff:", self.attackpoints,
              "\n| Verteidigung:", self.defencepoints,
              "\n| Torwart:", self.keeperpoints,"\n---------------"
              )
