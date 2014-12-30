# To start from within PythonShell 3.4.2 type:
#
# exec(open("./MannschaftsGenerator.py").read())
#
import Team
import Player


def menue():
    print ('--- Menü ---')
    print ('Drücke die 1 um einen Spieler hinzuzufügen')
    print ('Drücke die 2 um einen Spieler zulöschen')
    print ('Drücke die 3 um dir alle Spieler anzeigenzulassen')
    menueInput = input('... und bestatige mit Enter\n')
    print (menueInput)
    
    
   # while menueInput != '1' and menueInput != '2' and menueInput != '3':
   #     menueInput = input('1, 2 oder 3 - ist das so schwer?\n')
   #     print (menueInput)
    print ('cool')
    
        
    if menueInput == 1:
            pass
    elif menueInput == 2:
            pass

#==============================================================================
# print("--- MannschaftsGenerator ---")
# otto = Player.Player("Otto", 10 ,200, 40)
# popo = Player.Player("Popo", 40, 0, 10)
# otto2 = Player.Player("Otto")
# 
# print ("Spieler 1:")
# otto.print()
# 
# print("Spieler 2:")
# popo.print()
# 
# 
# teamA = Team.Team("A-Team")
# teamB = Team.Team("B-Team")
# 
# teamA.addPlayer(otto)
# teamA.addPlayer(popo)
# teamA.addPlayer(popo)
# teamA.print()
# #
# print ("Jetzt fliegt Otto raus!")
# teamA.removePlayer(otto)
# #teamA.removePlayer(otto)
# teamA.print()
# print(teamA.calcTeampoints())
# print(teamA.calcTeampoints())
# print(teamA.calcTeampoints())
#==============================================================================


#print("--- Ende ---")