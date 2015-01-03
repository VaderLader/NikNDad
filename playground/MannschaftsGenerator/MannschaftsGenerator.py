#To start from within PythonShell 3.4.2 type:
#
#exec(open("/home/pi/GitHub/NikNDad/playground/MannschaftsGenerator/MannschaftsGenerator.py").read())
#
import Team
import Player
import json_object_en_n_decoder as myjason

def menue():
    
    print ('--- Menü ---')
    print ('Drücke die 1 um einen Spieler hinzuzufügen')
    print ('Drücke die 2 um einen Spieler zulöschen')
    print ('Drücke die 3 um dir alle Spieler anzeigenzulassen')
    menueInput = int(input('... und bestatige mit Enter\n'))
    print (menueInput)
    
    stopp = 0
    while (menueInput != 1) and (menueInput != 2) and (menueInput != 3) and (menueInput != 4):
        menueInput = int(input('1, 2 oder 3 - ist das so schwer?\n'))
        print (menueInput)
        stopp += 1
        if stopp == 4:
            menueInput = 4
    print ('cool')
    
        
    if menueInput == 1:
        p = teamA.inputPlayer()
        teamA.addPlayer(p)
        
    elif menueInput == 2:
            p = input('Welchen Spieler willst du löschen')
            teamA.removePlayer(p)
    elif menueInput == 3:
        teamA.print()
    elif menueInput == 4:
        stopp = 4
    
    if stopp == 4:
        print ('Ich hab die Schnautze voll')
    else:
        menue()



#menue()


#==============================================================================
print("--- MannschaftsGenerator ---")
Otto = Player.Player("Otto", 10 ,200, 40)
Popo = Player.Player("Popo", 40, 0, 10)
otto2 = Player.Player("Otto")

print ("Spieler 1:")
Otto.print()

print ("Print by using ""Otto.__dict__"":\n", Otto.__dict__)

print("Spieler 2:")
Popo.print()


teamA = Team.Team("A-Team")
teamB = Team.Team("B-Team")

teamA.addPlayer(Otto)
teamA.addPlayer(Popo)
teamA.addPlayer(Popo)
teamA.print()
#
print ("Jetzt fliegt Otto raus!")
#teamA.removePlayer(Otto)
#teamA.removePlayer(otto)
#teamA.print()
#print(teamA.calcTeampoints())
#print(teamA.calcTeampoints())
#print(teamA.calcTeampoints())
#==============================================================================


#print("--- Ende ---")

#menue()

#print (myjason.MyEncoder().encode(teamA))


#encoded_object = myjason.MyEncoder().encode(teamA)
#print ("-----\nencoded_object:\n")
#print (encoded_object)
#print ("----- Endocing finished !!-----------\n")

#print ("----Calling decoder ----")
#myobj_instance = myjason.MyDecoder().decode(encoded_object)
#print ("---- decoded object:\n")
#print (myobj_instance)
##.print())




