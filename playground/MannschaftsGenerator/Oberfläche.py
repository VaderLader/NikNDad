# -*- coding: utf-8 -*-

#import MannschaftsGenerator
import TeamGenerator
#import Team
import Player
import json_object_en_n_decoder as myjson #There jason is imported
#import itertools


import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.uic import *


def startWeiter():
    s1.close()
    s2.show()


def add():
    print('add() in Oberfläche')
    maxErreicht.show()
    maxErreicht.okBtn.clicked.connect(maxErreicht.close) 

#==============================================================================   
    
def weiterRechnen():
    ''' weiterRechnen() function triggert by clicking "Weiter"-button '''    
    #print('Called weiterRechnen in Oberfläche')
    
    ##################
    'Read in data with the right data types from the form'
    'into some lists, which can be used easily afterwards'
    name=[s2.lineEdit_1.text(), s2.lineEdit_2.text(), s2.lineEdit_3.text(),
          s2.lineEdit_4.text(), s2.lineEdit_5.text(), s2.lineEdit_6.text(),
          s2.lineEdit_7.text(), s2.lineEdit_8.text()]
    angriff=[int(s2.spinBox_1a.text()), int(s2.spinBox_2a.text()),
             int(s2.spinBox_3a.text()), int(s2.spinBox_4a.text()), 
             int(s2.spinBox_5a.text()), int(s2.spinBox_6a.text()),
             int(s2.spinBox_7a.text()), int(s2.spinBox_8a.text())]
    abwehr=[int(s2.spinBox_1d.text()), int(s2.spinBox_2d.text()),
            int(s2.spinBox_3d.text()), int(s2.spinBox_4d.text()), 
            int(s2.spinBox_5d.text()), int(s2.spinBox_6d.text()),
            int(s2.spinBox_7d.text()), int(s2.spinBox_8d.text())]
    tor=[int(s2.spinBox_1g.text()), int(s2.spinBox_2g.text()),
         int(s2.spinBox_3g.text()), int(s2.spinBox_4g.text()), 
         int(s2.spinBox_5g.text()), int(s2.spinBox_6g.text()),
         int(s2.spinBox_7g.text()), int(s2.spinBox_8g.text())]
    check=[s2.checkBox_1.checkState(), s2.checkBox_2.checkState(),
           s2.checkBox_3.checkState(), s2.checkBox_4.checkState(), 
           s2.checkBox_5.checkState(), s2.checkBox_6.checkState(),
           s2.checkBox_7.checkState(), s2.checkBox_8.checkState()]
    ##################
    
    sq = s2.lineEdit_1.text()
    print('sq=[',sq,']')

    MannschaftsGenerator.defMannschaften()
    
    for index, element in enumerate(name):
        print('check[index]=', 'check[',index,']=',check[index])
        if check[index] == 2:
            print('index=',index)
            print('name[',index,']=',name[index])
            print('angriff[',index,']=',angriff[index])
            
            teamA.addPlayer( Player.Player({'name': name[index],
                                'attackpoints': angriff[index],
                                'defencepoints': abwehr[index], 
                                'keeperpoints': tor[index]}) )
    
    MannschaftsGenerator.berechneMannschaften()
    
    print('weiterRechnen: teamA.Mitglieder=')
    steam = teamA.print()
    print(steam)
    s2.close()
    showTeams.show()
    showTeams.showA.setText(str(steam))
    showTeams.showB.setText(str(teamA.Mitglieder)) # TODO later "B"
    #showTeams.show()
    


# Main program
# main
print('---- START ----')
tg = TeamGenerator() 

app = QApplication(sys.argv)
s1 = loadUi('Oberfläche.ui')
s2 = loadUi('Oberfläche2.ui')
maxErreicht = loadUi('maxAnzahlErreicht.ui')
showTeams = loadUi('showTeams.ui')

# Show first UI Screen

print('---- Load both teams as they have been the saved to file ----')
tg.loadTeams('./')

print(tg.teamA.print())
print(tg.teamB.print())
print('---- Shift players from teamB to teamA ----')
tg.teamA.shiftPlayersFromTeam(tg.teamB)
print(tg.teamA.print())
print(tg.teamB.print())
print('---- berechneMannschaften ')
tg.berechneMannschaften()
print(tg.teamA.print())
print(tg.teamB.print())
print('---- berechneMannschaften ')
tg.dumpTeams('./Result/')
print('---- ')


print('---- END ----')

###
#print('Reading TeamA from file')
#f = open("./ATeam_3P.json","r")
#teamA = myjson.OrderedDecoder().decode(f.read())
#print('teamA loaded from file:')
#teamA.print()
#print()
###


print('s1.show()')
s1.show()

print('s1.startWeiterBtn.clicked.connect(startWeiter)')
s1.startWeiterBtn.clicked.connect(startWeiter)

print('s2.addBtn.clicked.connect(add)')
s2.addBtn.clicked.connect(add)

print('s2.zweiWeiterBtn.clicked.connect(weiterRechnen)')
s2.zweiWeiterBtn.clicked.connect(weiterRechnen)

print('app.exec_()')
sys.exit(app.exec_())