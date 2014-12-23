class Player:
    '''Class for Players'''
    def __init__(self, i_name = "Vorname Name", i_attackrank = 0, i_defencerank = 0, i_keeperrank = 0):
        self.name = i_name
        self.attackrank = i_attackrank
        self.defecerank = i_defencerank
        self.keeperrank = i_keeperrank

    def print(self):
        print("Spieler:", self.name, "\nAngriff:", self.attackrank)
