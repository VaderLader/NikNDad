# -*- coding: utf-8 -*-
import MannschaftsGenerator
import Team
import Player

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.uic import *

app = QApplication(sys.argv)
s1 = loadUi('Oberfläche.ui')
s2 = loadUi('Oberfläche2.ui')
maxErreicht = loadUi('maxAnzahlErreicht.ui')
showTeams = loadUi('showTeams.ui')

def startWeiter():
    s1.close()
    s2.show()
    
name=[s2.lineEdit_1, s2.lineEdit_2, s2.lineEdit_3, s2.lineEdit_4, s2.lineEdit_5, s2.lineEdit_6, s2.lineEdit_7, s2.lineEdit_8]
angriff=[s2.spinBox_1a,s2.spinBox_2a,s2.spinBox_3a,s2.spinBox_4a,s2.spinBox_5a,s2.spinBox_6a,s2.spinBox_7a,s2.spinBox_8a]
abwehr=[s2.spinBox_1d,s2.spinBox_2d,s2.spinBox_3d,s2.spinBox_4d,s2.spinBox_5d,s2.spinBox_6d,s2.spinBox_7d,s2.spinBox_8d]
tor=[s2.spinBox_1g,s2.spinBox_2g,s2.spinBox_3g,s2.spinBox_4g,s2.spinBox_5g,s2.spinBox_6g,s2.spinBox_7g,s2.spinBox_8g]
check=[s2.checkBox_1, s2.checkBox_2, s2.checkBox_3, s2.checkBox_4, s2.checkBox_5, s2.checkBox_6, s2.checkBox_7, s2.checkBox_8]

geoY = 50



def add():
    print('add() in Oberfläche')
    maxErreicht.show()
    maxErreicht.okBtn.clicked.connect(maxErreicht.close) 
#==============================================================================
#     print ('add')
#     btn = QPushButton('Text')
#     btn.setGeometry(20, 50, 60, 60)
#==============================================================================
   # geoY += 10
#==============================================================================
#      quit = QtGui.QPushButton('Close', self)
#  quit.setGeometry(10, 10, 60, 35)
#==============================================================================
    
def weiterRechnen():
    print('Called weiterRechnen in Oberfläche')
    MannschaftsGenerator.defMannschaften()
    
    for index, element in enumerate(name):
        if check[index] == True:
            print('index=',index)
            print('name[index]=',name[index])
            print('angriff[index]=',angriff[index])
            
            MannschaftsGenerator.teamA.addPlayer( Player.Player({'name': name[index],
                                'attackpoints': angriff[index],
                                'defencepoints': abwehr[index], 
                                'keeperpoint': tor[index]}) )
    
    MannschaftsGenerator.berechneMannschaften()
    
    print('MannschaftsGenerator.teamA.Mitglieder=', MannschaftsGenerator.teamA.Mitglieder)
    s2.close()
    showTeams.show()
    showTeams.showA.setText(str(MannschaftsGenerator.teamA.Mitglieder))
    showTeams.showB.setText(str(MannschaftsGenerator.teamB.Mitglieder))
    #showTeams.show()
    
    


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