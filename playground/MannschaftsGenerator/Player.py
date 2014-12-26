class Player:
    '''Class for Players'''
    player_counter = 0  # static member
    
    def __init__(self, i_name = "Vorname Name", i_attackrank = 0, i_defencerank = 0, i_keeperrank = 0):
        self.name = i_name
        self.attackrank = i_attackrank
        self.defecerank = i_defencerank
        self.keeperrank = i_keeperrank
        Player.player_counter += 1
        
    def print(self):
        print("--",  "Spieler:", self.name, "--",
              "\n| Angriff:", self.attackrank,
              "\n| Verteidigung:", self.defecerank,
              "\n| Torwart:", self.keeperrank,"\n---------------"
              )
