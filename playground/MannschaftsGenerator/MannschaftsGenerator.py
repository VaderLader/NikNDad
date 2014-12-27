# To start from within PythonShell 3.4.2 type:
#
# exec(open("./MannschaftsGenerator.py").read())
#
import Team
import Player

print("--- MannschaftsGenerator ---")
otto = Player.Player("Otto")
popo = Player.Player("Popo")

print("Spieler 1:")
otto.print()

print("Spieler 2:")
popo.print()


teamA = Team.Team("A-Team")
teamB = Team.Team("B-Team")

teamA.addPlayer(otto)
teamA.addPlayer(popo)
teamA.print()
#
print ("Jetzt fliegt Otto raus!")
teamA.removePlayer(otto)
teamA.print()
print("--- Ende ---")

