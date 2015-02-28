# -*- coding: utf-8 -*-
"""
Created on Sat Feb 28 16:43:55 2015

@author: pi
"""

import sys
import PyQt4.QtCore as QtCore
from PyQt4.QtGui import *
from PyQt4.uic import *

import TeamGenerator

class TeamGeneratorModel(QtCore.QAbstractListModel):

    def ___init__(self, team = [], parent = None):
        QtCore.QAbstractListModel.__init__(self, parent)
        self.__team = team
        
    def headerData(self, section, orientation, role):
        
        if role == QtCore.Qt.DisplayRole:
            
            if orientation == QtCore.Qt.Horizontal:
                return QtCore.QString("Spieler Name")
            else:
                return QtCore.QString("Spieler %1").arg(section + 1)   
    
    def data(self, index, role):
        
        
        if role == QtCore.Qt.EditRole:
            return self.__colors[index.row()].name()

    

if __name__ == '__main__':
    
    print('----- START -----')
    
    app = QApplication(sys.argv)
    s1 = loadUi('./.GUI/GUI_Number_1.ui')
    
    s1.show()
   
    
    tg = TeamGenerator.TeamGenerator()
    print('---- Load both teams as they have been the saved to file ----')
    tg.loadTeam('fullTeam','./Input/', 'FullTeam.json')
    tgm = TeamGeneratorModel(["1","2"]) #tg.fullTeam)
    
    s1.tableView_A.setModel(tgm)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    print('----- END -----')
    
    sys.exit(app.exec_())
    
    print('----- STOP -----')