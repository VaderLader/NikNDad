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
        ''' Constructor: TeamGenerator() '''
        self.teamA = Team.Team({'name': 'A-Team', 
                                'players': []
                                })
        self.teamB = Team.Team({'name': 'B-Team', 
                                'players': []
                                })
        self.fullTeam = Team.Team({'name': 'Full-Team', 
                                'players': []
                                })
        
#==============================================================================            
    def berechneMannschaften(self):
        ''' Method to calculate and select two teams which are most equal '''
        print ("In berechneMannschaften()")
        if len(self.teamA.players)%2 != 0:
            self.teamA.addPlayer(Player.Player({'name': 'NullPlayer',
                                           'attackpoints': 0,
                                           'defencepoints': 0, 
                                           'keeperpoints': 0}))
        
        spielerliste = list(range(0,len(self.teamA.players))) 
        #print("self.teamA.players=",spielerliste)
        
        # lTeamA keeps the List of all possible TeamAs, wich can be setup
        # with different player combinations        
        combos = itertools.combinations(list(range(0,len(self.teamA.players))),
                                        int(len(self.teamA.players)/2))
        lTeamA = list(combos)  
        print("Anzahl der verschiedenen Teams = ", len(lTeamA)) 
        #print("Verschiedene Teams lTeamA =",lTeamA)
        
        # Erzeuge das jeweils passenden Team B
        lTeamB = []
        for e in lTeamA:
            dummy = list(spielerliste)
            #print("e=",e)
            for p in e:
              #  print ("p=",str(p))
                dummy.pop(dummy.index(p))
            lTeamB.append(list(dummy))
        #print("lTeamB =",lTeamB)

        # Berechnung von der Teamstärkendifferenz
        teampointsDif = []
             
        
        for e in lTeamA:
            tDif  = 0
            for p in e:
                tDif += self.teamA.players[p].playerpoints
            teampointsDif.append(tDif)
        #print("teampointsDif=",teampointsDif)
        
        index = 0
        for e in lTeamB:
            tDif  = 0
            for p in e:
                #print ("p=",p)
                tDif += self.teamA.players[p].playerpoints
            teampointsDif[index] = abs(teampointsDif[index] - tDif)
            index = index +1
        print("len(teampointsDif)=",len(teampointsDif))
        #print("teampointsDif=",teampointsDif)
        
       
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

        # Shift Players from teamA to teamB
        #     
        poplist = list(lTeamB[indexmin])
        #print("poplist=",poplist)
        poplist.sort(reverse=True)
        #print("poplist=",poplist)
        
        for e in  poplist:
            self.teamB.addPlayer(self.teamA.removeByIndex(e))
        
        self.teamA.print()
        self.teamB.print()          
        print("End of berechneMannschaften()")
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
        ''' method to write the two teams to disk '''
        print ("-------- Calling dumpTeams(",location, ") ----")
        # teamA
        self.dumpTeam('teamA', location, 'ATeam.json')
      
        # teamB
        self.dumpTeam('teamB', location, 'BTeam.json')
        
        print ("----- Encoding finished and written to file !!!-----------\n")
        
    def dumpTeam(self, teamName, location, filename):
        ''' dumpTeam(<Name of the Team Variable>, <filesystem path>,
                     <jason filename>) '''        
        encoded_object = myjson.OrderedEncoder().encode(self.__dict__[teamName])
        s = str(location + filename)        
        f = open(s,"w")
        print("File '", s,"' written with ", f.write(encoded_object)," Chars")
        f.flush()
        
    def loadTeam(self, teamName, location, filename):
        ''' loadTeam(<Name of the Team Variable>, <filesystem path>,
                     <jason filename>)'''
        s = str(location + filename)         
        f = open(s,"r")
        self.__dict__[teamName] = myjson.OrderedDecoder().decode(f.read())
        print('self.__dict__[teamName]= ',self.__dict__[teamName].print())
        
        print('-------- loadTeam: self.__dict__[',teamName,'].print()\n',
              self.__dict__[teamName].print())
        print('-------- loadTeam: self.fullTeam.print()',self.fullTeam.print(),'\n')
              
        
    def loadTeams(self, location):    
        ''' method to load the two teams from disk '''
        print ("-------- Calling loadTeams(",location, ") --------")
        
        # teamA
        self.loadTeam('teamA', location, "ATeam.json")
        #print(self.teamA.print())
        
        # teamB        
        self.loadTeam('teamB', location, "BTeam.json")        
        #print(self.teamB.print())
     
# main
if __name__ == '__main__':
    
    
    print('---- START ----')
    tg = TeamGenerator() 
    x = 45
    
    #tg.sampleTeamSetup()
    print('---- Load all Players into "fullTeam" as they have been the saved to file ----')
    tg.loadTeam('fullTeam','./Input/', 'VerySmallTeam.json')
    print('---+++', tg.fullTeam.print())
    tg.dumpTeam('fullTeam','./Input/', 'VerySmallTeam_out.json')
    #print('---+++', tg.fullTeam.print())
    #print(tg.teamA.print())
    #print(tg.teamB.print())
    print('\n---- Shift players from fullTeam to teamA ----')
    print('len(tg.fullTeam.players)', len(tg.fullTeam.players))
    tg.teamA.shiftNPlayersFromTeam(tg.fullTeam,len(tg.fullTeam.players))
    print('\n------\n')    
    print('---teamA---\n', tg.teamA.print())
    print('\n------\n')    
    print('---teamB---\n', tg.teamB.print())
    print('\n------\n')
    print('---- berechneMannschaften ')
    tg.berechneMannschaften()
    print('\n---- Result after berechneMannschaften:\n')
    print(tg.teamA.print())
    print(tg.teamB.print())
    print('---- dumpTeams ')
    tg.dumpTeams('./Result/')
    print('---- ')
    
    
    print('---- END ----')
    