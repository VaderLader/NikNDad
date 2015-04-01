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

class TeamGeneratorModel(QtCore.QAbstractTableModel):

    def __init__(self, ptable = [], parent = None):
        QtCore.QAbstractTableModel.__init__(self, parent)
        self.__ptable = ptable
        

        
        
    def sortColumn(section):
        pass    
        
    def headerData(self, section, orientation, role):
        
        if role == QtCore.Qt.DisplayRole:
            
            if orientation == QtCore.Qt.Horizontal:
                if section == 0:                
                    return "Spieler Name"
                elif section == 1:
                    return 'Angriff'
                elif section == 2:
                    return 'Abwehr'
                elif section == 3:
                    return 'Tor'
                elif section == 4:
                    return 'Gesammt'
                    
            else:                
                return "Spieler " + str(section)  
    
    def data(self, index, role):
        row = index.row()
        column = index.column()
        
        if role == QtCore.Qt.DisplayRole:
            if column == 0:
                return str(self.__ptable[row].name)
            elif column == 1:
                return int(self.__ptable[row].attackpoints)                
            elif column == 2:
                return int(self.__ptable[row].defencepoints) 
            elif column == 3:
                return int(self.__ptable[row].keeperpoints) 
            elif column == 4:
                return float("%.2f" % self.__ptable[row].playerpoints)

                
        if role == QtCore.Qt.EditRole:
            return self.__ptable[row].name
            
    def rowCount(self, parent):
        return len(self.__ptable)
        
    def columnCount(self, parent):
        return 5
    
    def flags(self,index): 
        return QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable
        
    def setData(self, index, value, role = QtCore.Qt.EditRole):
       # setData is always called if data has to be displayed 
        s1.gesammt_A.setText("%.2f" % tg.teamA.calcTeampoints())
        s1.gesammt_B.setText("%.2f" % tg.teamB.calcTeampoints())
        if role == QtCore.Qt.EditRole:
            
            row = index.row()
            column = index.column()
            
            if column == 0:
                self.__ptable[row].name = str(value)
            elif column == 1:
                self.__ptable[row].attackpoints = int(value) 
            elif column == 2:
                self.__ptable[row].defencepoints = int(value)
            elif column == 3:
                self.__ptable[row].keeperpoints = int(value) 
            
            self.__ptable[row].calcPlayerpoints()
            return True
        return False
        
    def insertRows(self, position, rows, parent = QtCore.QModelIndex()):
        # Syntax: self.beginInsertRows(index,first,last)
        self.beginInsertRows(parent, position, position + rows - 1)  
        newPlayer = TeamGenerator.Player.Player({'name': '<Neuer Spieler>',
                                          'attackpoints': 0,
                                          'defencepoints': 0, 
                                          'keeperpoints': 0})        
        self.__ptable.insert(position,newPlayer)

        self.endInsertRows()
        return True
        
    def removeRows(self, position, rows, parent = QtCore.QModelIndex()):
        self.beginRemoveRows(parent, position, position + rows - 1)
        
        for i in range(rows):
            value = self.__ptable[position]
            self.__ptable.remove(value)
             
        self.endRemoveRows()
        return True

    
#==============================================================================
    def sort(self, Ncol, order):
         """Sort table by given column number.
         """
         #self.emit(SIGNAL("layoutAboutToBeChanged()"))
         self.__ptable = sorted(self.__ptable, key=operator.itemgetter(Ncol))        
         if order == Qt.DescendingOrder:
             self.arraydata.reverse()
         self.emit(SIGNAL("layoutChanged()"))
#==============================================================================
 
class PlayerFilterProxyModel(QSortFilterProxyModel):
    pass
       


def insertClicked():
    
    tgmA.insertRows(0,1)        
    #TODO:
    #Abhängig vom Focus entweder TeamA Tabelle oder TeamB Tabelle erweitern    
    #tgmB.insertRows(0,1)        
    refreshGUI()    

    
def tableClick():
    print ('§§§§§§§§§§§§§§§§§§§TABLE CLICKED §§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§')


def headerClick():
    print ('Header Click')
    
 
def callBerechneManschaften():
    print("### callBerechneManschaften() ###")
    tg.berechneMannschaften()    
    print("########### TEAM A: ############")
    tg.teamA.print()
    print("########### TEAM B: ############")
    tg.teamB.print()
    refreshGUI()    


    
def refreshGUI():
    s1.gesammt_A.setText("%.2f" % tg.teamA.calcTeampoints())
    s1.gesammt_B.setText("%.2f" % tg.teamB.calcTeampoints())
    
    tgmA = TeamGeneratorModel(tg.teamA.players)
    tgmB = TeamGeneratorModel(tg.teamB.players)
    s1.tableView_A.setModel(tgmA)
    s1.tableView_B.setModel(tgmB)

    proxyA = PlayerFilterProxyModel(tgmA)
    proxyA.setSourceModel(tgmA)
    s1.tableView_A.setModel(proxyA)  
    
    proxyB = PlayerFilterProxyModel(tgmB)
    proxyB.setSourceModel(tgmB) 
    s1.tableView_B.setModel(proxyB)
    


if __name__ == '__main__':
  
 
   
    
    print('----- START -----')
    
    app = QApplication(sys.argv)
    s1 = loadUi('./.GUI/GUI_Number_1.ui')
        
    s1.show()
    
    
    tg = TeamGenerator.TeamGenerator()
    print('---- Load both teams as they have been the saved to file ----')
    tg.loadTeam('teamA','./Input/', 'SmallTeam.json')

    print("########### TEAM A: ############")
    tg.teamA.print()
    print("########### TEAM B: ############")
    tg.teamB.print()
    
    print("########### TEST START ############")
    #print(str(p.name) for p in tg.fullTeam.players)    
    #print("++++++++++++++++++")
    
  
    tgmA = TeamGeneratorModel(tg.teamA.players)#[[tg.fullTeam.players.name], [tg.fullTeam.players.attackpoints], [tg.fullTeam.players.defencepoints]] ) #     ['1', '2', '3'])
    tgmB = TeamGeneratorModel(tg.teamB.players)
    
    s1.gesammt_A.setText(str(tg.teamA.calcTeampoints()))
    s1.gesammt_B.setText(str(tg.teamB.calcTeampoints()))
    
       
    s1.tableView_A.setModel(tgmA)
    s1.tableView_B.setModel(tgmB)
    
    s1.pushButton_2.clicked.connect(insertClicked)
    s1.pushButton_1.clicked.connect(callBerechneManschaften)  

   
    
    proxyA = PlayerFilterProxyModel(tgmA)
    proxyA.setSourceModel(tgmA)
    s1.tableView_A.setModel(proxyA)  
    
    proxyB = PlayerFilterProxyModel(tgmB)
    proxyB.setSourceModel(tgmB) 
    s1.tableView_B.setModel(proxyB)
     
    
    
    print('----- END -----')
    
    sys.exit(app.exec_())
    
    print('----- STOP -----')