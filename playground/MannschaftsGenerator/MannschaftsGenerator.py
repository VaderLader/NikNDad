import Team
import Player

print("--- MannschaftsGenerator ---")
otto = Player.Player("Otto")
popo = Player.Player("Popo")

print("Spieler 1:")
otto.print()

print("Spiler 2:")
popo.print()


teamA = Team.Team("A-Team")
teamB = Team.Team("B-Team")

teamA.addPlayer(otto)
teamA.addPlayer(popo)
teamA.print



print("--- Ende ---")

    