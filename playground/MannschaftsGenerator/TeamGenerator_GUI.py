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

    def __init__(self, player = [], parent = None):
        QtCore.QAbstractListModel.__init__(self, parent)
        self.__player = player
        
    def headerData(self, section, orientation, role):
        
        if role == QtCore.Qt.DisplayRole:
            
            if orientation == QtCore.Qt.Horizontal:
                return "Spieler Name"
            else:                
                return "Spieler " + str(section + 1)  
    
    def data(self, index, role):
        print('data(self, index, role):')
        if role == QtCore.Qt.DisplayRole:
            print('True')
            return str( self.__player[index.row()].name)
        else:
            print('False')
            
            
    def rowCount(self, parent):
        return len(self.__player)
    
    def flags(self,index): 
        return QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable
        
    

if __name__ == '__main__':
    
    print('----- START -----')
    
    app = QApplication(sys.argv)
    s1 = loadUi('./.GUI/GUI_Number_1.ui')
    
    s1.show()
   
    
    tg = TeamGenerator.TeamGenerator()
    print('---- Load both teams as they have been the saved to file ----')
    tg.loadTeam('fullTeam','./Input/', 'FullTeam.json')
    tgm = TeamGeneratorModel(tg.fullTeam.players) #     ['1', '2', '3'])
    
    s1.tableView_A.setModel(tgm)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    print('----- END -----')
    
    sys.exit(app.exec_())
    
    print('----- STOP -----')