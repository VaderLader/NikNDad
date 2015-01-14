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
    
name=[s2.lineEdit_1,s2.lineEdit_2,s2.lineEdit_3,s2.lineEdit_4,s2.lineEdit_5,s2.lineEdit_6,s2.lineEdit_7,s2.lineEdit_8]
angriff=[s2.spinBox_1a,s2.spinBox_2a,s2.spinBox_3a,s2.spinBox_4a,s2.spinBox_5a,s2.spinBox_6a,s2.spinBox_7a,s2.spinBox_8a]
abwehr=[s2.spinBox_1d,s2.spinBox_2d,s2.spinBox_3d,s2.spinBox_4d,s2.spinBox_5d,s2.spinBox_6d,s2.spinBox_7d,s2.spinBox_8d]
tor=[s2.spinBox_1g,s2.spinBox_2g,s2.spinBox_3g,s2.spinBox_4g,s2.spinBox_5g,s2.spinBox_6g,s2.spinBox_7g,s2.spinBox_8g]
check=[s2.checkBox_1,s2.checkBox_2,s2.checkBox_3,s2.checkBox_4,s2.checkBox_5,s2.checkBox_6,s2.checkBox_7,s2.checkBox_8]

geoY = 50



def add():
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
    MannschaftsGenerator.defMannschaften()
    
    for index in name:
        if check[index] == 1:
            Mannschaftsgenerator.teamA.addPlayer( Player.Player({'name': name[index],
                                'attackpoints': angriff[index],
                                'defencepoints': abwehr[index], 
                                'keeperpoint': tor[index]}) )
        MannschaftsGenerator.macheMannschaften()
        
        s2.close()
        showTeams.showA.setText(Mannschaftsgenerator.teamA.Mitglieder)
        showTeams.showB.setText(Mannschaftsgenerator.teamB.Mitglieder)
    
    
    



s1.show()

s1.startWeiterBtn.clicked.connect(startWeiter)

s2.addBtn.clicked.connect(add)
s2.zweiWeiterBtn.clicked.connect(weiterRechnen)


sys.exit(app.exec_())