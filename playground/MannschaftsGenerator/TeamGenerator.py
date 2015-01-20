#To start from within PythonShell 3.4.2 type:
#
#exec(open("/home/pi/GitHub/NikNDad/playground/MannschaftsGenerator/MannschaftsGenerator.py").read())
#
import Team
import Player
import json_object_en_n_decoder as myjson #There jason is imported
import itertools


class TeamGenerator:
    ''' TeamGenerator class for Calculating best team distributions '''   

    def __init__(self):
        self.teamA = Team.Team({'name': 'A-Team', 
                                'players': []
                                })
        self.teamB = Team.Team({'name': 'B-Team', 
                                'players': []
                                })
        
#==============================================================================            
    def berechneMannschaften(self):
        if len(self.teamA.players)%2 != 0:
            self.teamA.addPlayer(Player.Player({'name': 'NullPlayer',
                                           'attackpoints': 0,
                                           'defencepoints': 0, 
                                           'keeperpoints': 0}))
        
        spielerliste = list(range(0,len(self.teamA.players))) 
        print (spielerliste)
        print("self.teamA.players=",list(range(0,len(self.teamA.players))))
        combos = itertools.combinations(list(range(0,len(self.teamA.players))),
                                        int(len(self.teamA.players)/2))
        lTeamA = list(combos) #
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
                tDif += self.teamA.players[p].playerpoints
                print("tDif=",tDif)
            teampointsDif.append(tDif)
        print("teampointsDif=",teampointsDif)
        
        index = 0
        for e in lTeamB:
            tDif  = 0
            for p in e:
                #print ("p=",p)
                tDif += self.teamA.players[p].playerpoints
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
            self.teamB.addPlayer(self.teamA.removeByIndex(e))
        
        self.teamA.print()
        self.teamB.print()          
    
#==============================================================================
    
    def sampleTeamSetup(self):
        ''' Method to initial the two teams with dummy data'''
        print('-------- sampleTeamSetup called ----')
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
        self.teamA.addPlayer(Otto)
        self.teamA.addPlayer(Popo)
        self.teamA.addPlayer(Roko)
        self.teamA.addPlayer(Beka)
        print(self.teamA.print())
   
#==============================================================================
    
    def dumpTeams(self, location='./'):
        ''' method to write the tow teams to disk '''
        print ("----Calling dumpTeams(",location, ") ----")
        # teamA
        encoded_object = myjson.OrderedEncoder().encode(self.teamA)
        print ("-----\nencoded_object:\n")
        print (encoded_object)
        f = open(str(location + "ATeam.json"),"w")
        print("# Chars written to file:", f.write(encoded_object))
        f.flush()
        
        # teamB
        encoded_object = myjson.OrderedEncoder().encode(self.teamB)
        print ("-----\nencoded_object:\n")
        print (encoded_object)
        f = open(str(location + "BTeam.json"),"w")
        print("# Chars written to file:", f.write(encoded_object))
        f.flush()
                
        
        print ("----- Encoding finished and written to file !!!-----------\n")
    
    def loadTeams(self, location):    
        ''' method to load the two teams from disk '''
        print ("----Calling loadTeams(",location, ") ----")
        
        # teamA
        f = open(str(location + "ATeam.json"),"r")
        self.teamA = myjson.OrderedDecoder().decode(f.read())
        #print(self.teamA.print())
        
        # teamB        
        f = open(str(location + "BTeam.json"),"r")
        self.teamB = myjson.OrderedDecoder().decode(f.read())
        #print(self.teamB.print())
    
    
# main
print('---- START ----')
tg = TeamGenerator() 

#tg.sampleTeamSetup()

tg.loadTeams('./')

print(tg.teamA.print())
print(tg.teamB.print())

print('---- END ----')
