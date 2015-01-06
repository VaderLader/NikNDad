#To start from within PythonShell 3.4.2 type:
#
#exec(open("/home/pi/GitHub/NikNDad/playground/MannschaftsGenerator/MannschaftsGenerator.py").read())
#
import Team
import Player
import json_object_en_n_decoder as myjson #There jason is imported
import itertools


def menue():
    
    print ('--- Menü ---')
    print ('Drücke die 1 um einen Spieler hinzuzufügen')
    print ('Drücke die 2 um einen Spieler zulöschen')
    print ('Drücke die 3 um dir alle Spieler anzeigenzulassen') 
    menueInput = input('... und bestatige mit Enter\n')
    print (menueInput)
 
    type(menueInput)
    stopp = 0
    
        
    while (menueInput != 1) and (menueInput != 2) and (menueInput != 3) and (menueInput != 4):
        menueInput = input('1, 2 oder 3 - ist das so schwer?\n')
        print (menueInput)
        type(menueInput)        
        
        stopp += 1
        if stopp == 4:
            menueInput = 4
    print ('cool')
    
        
    if menueInput == 1:
        p = teamA.inputPlayer()
        teamA.addPlayer(p)
        
    elif menueInput == 2:
        n = input('Welchen Spieler willst du löschen')
        teamA.removeName(n)
            
    elif menueInput == 3:
        teamA.print()
    elif menueInput == 4:
        stopp = 4
    
    if stopp == 4:
        print ('Ich hab die Schnautze voll')
    else:
        menue()
        
def macheManschaften():
    if len(teamA.players)%2 != 0:
        teamA.addPlayer(Player.Player('nullSpieler', 0, 0, 0))
    
    spielerliste = list(range(0,len(teamA.players))) 
    print (spielerliste)
    print("teamA.players=",list(range(0,len(teamA.players))))
    combos = itertools.combinations(list(range(0,len(teamA.players))), int(len(teamA.players)/2))
    lTeamA = list(combos)
    print("lTeamA=",lTeamA)
    lTeamB = []
    
    # Erzeuge das jeweils passenden Team B
    for e in lTeamA:
        dummy = list(spielerliste)
        #print("e=",e)
        for p in e:
          #  print ("p=",str(p))
            dummy.pop(dummy.index(p))
        lTeamB.append(list(dummy))
    print("lTeamB=",lTeamB)
    # Berechnung von der Teamstärkendifferenz
    teampointsDif = []
    
    for e in lTeamA:
        tDif  = 0
        for p in e:
            print("tDif=",tDif)
            tDif += teamA.players[p].playerpoints
            print("tDif=",tDif)
        teampointsDif.append(tDif)
    print("teampointsDif=",teampointsDif)
    
    index = 0
    for e in lTeamB:
        tDif  = 0
        for p in e:
            #print ("p=",p)
            tDif += teamA.players[p].playerpoints
        teampointsDif[index] = abs(teampointsDif[index] - tDif)
        index = index +1
    print("teampointsDif=",teampointsDif)
   
    # Search for the minimum difference
    indexmin = 0
    valuemin = teampointsDif[0]
    index = 0
    for e in teampointsDif:
        if e < valuemin:
            valuemin = e
            indexmin = index
        index = index + 1 
    print("Valuemin=", valuemin, "  indexmin=", indexmin)
    print("Best Team:", lTeamA[indexmin], " vs. ",lTeamB[indexmin])
    
    poplist = list(lTeamB[indexmin])
    print("poplist=",poplist)
    poplist.sort(reverse=True)
    print("poplist=",poplist)
    
    for e in  poplist:
        print("e=", e)
        teamB.addPlayer(teamA.removeByIndex(e))
    
    teamA.print()
    teamB.print()          
    
#menue()


#==============================================================================
print("--- MannschaftsGenerator ---")
Otto = Player.Player({'name': 'Otto de Motto',
                      'attackpoints': 10,
                      'defencepoints': 20, 
                      'keeperpoints': 30})
Popo = Player.Player({'name': 'Popo di Mare',
                      'attackpoints': 30,
                      'defencepoints': 10, 
                      'keeperpoints': 20})
Roko = Player.Player({'name': 'Roko de Popo',
                      'attackpoints': 50,
                      'defencepoints': 20, 
                      'keeperpoints': 30})
Beka = Player.Player({'name': 'Beka am Weka',
                      'attackpoints': 5,
                      'defencepoints': 20, 
                      'keeperpoints': 15})

print ("Spieler 1:")
#Otto.print()

#print ("Print by using ""Otto.__dict__"":\n", Otto.__dict__)

print("Spieler 2:")
#Popo.print()


teamA = Team.Team({'name': 'A-Team', 
                            'players': []
                            })
teamB = Team.Team({'name': 'B-Team', 
                            'players': []
                            })

teamA.addPlayer(Otto)
teamA.addPlayer(Popo)
teamA.addPlayer(Roko)
teamA.addPlayer(Beka)
#teamA.print()
#
#print ("Jetzt fliegt Otto raus!")
#teamA.removePlayer(Otto)
#teamA.removePlayer(otto)
#teamA.print()
#print(teamA.calcTeampoints())
#print(teamA.calcTeampoints())
#print(teamA.calcTeampoints())
#==============================================================================

macheManschaften()


#menue()

#print (myjson.MyEncoder().encode(teamA))


#encoded_object = myjson.MyEncoder().encode(teamA)
encoded_object = myjson.OrderedEncoder().encode(teamA)


print ("-----\nencoded_object:\n")
print (encoded_object)
f = open("./ATeam.json","w")
print("# Chars written to file:", f.write(encoded_object))
f.flush()
print ("----- Encoding finished and written to file !!!-----------\n")

print("---------------------------------------")

print ("----Calling decoder ----")
#myobj_instance = myjson.MyDecoder().decode(encoded_object)
myobj_instance = myjson.OrderedDecoder().decode(encoded_object)

print ("---- decoded object:\n")
#print (myobj_instance)
#myobj_instance.print()

f = open("./ATeam_3P.json","r")
TeamANew = myjson.OrderedDecoder().decode(f.read())
TeamANew.print()
print()
teamA.print()

'''
with open('filename.txt', 'r') as handle:
    parsed = json.load(handle)
'''

print("--- Ende ---")



