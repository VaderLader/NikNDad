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

    def __init__(self, ptable = [[]], parent = None):
#==============================================================================
#         print (ptable)
#         dummy = range(0, len(ptable))
#         print ([ptable,dummy,dummy,dummy,dummy])
#         print (ptable)
#         ptable = [ptable,dummy,dummy,dummy,dummy]
#==============================================================================
        QtCore.QAbstractTableModel.__init__(self, parent)
        dummy = range(0, len(ptable))
        self.__ptable = ptable
        
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
                return str(self.__ptable[0][row].name)
            elif column == 1:
                return str(self.__ptable[0][row].attackpoints)                
            elif column == 2:
                return str(self.__ptable[0][row].defencepoints) 
            elif column == 3:
                return str(self.__ptable[0][row].keeperpoints) 
            elif column == 4:
                return str(self.__ptable[0][row].playerpoints)
                
        if role == QtCore.Qt.EditRole:
            return self.__ptable[0][row].name()
            
    def rowCount(self, parent):
        return len(self.__ptable[0])
        
    def columnCount(self, parent):
        return len(self.__ptable)
    
    def flags(self,index): 
        return QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable
        
    def setData(self, index, value, role = QtCore.Qt.EditRole):
       
        
        if role == QtCore.Qt.EditRole:
            
            row = index.row()
            column = index.column()
            
            if column == 0:
                self.__ptable[0][row].name = str(value)
            elif column == 1:
                self.__ptable[0][row].attackpoints = int(value) 
            elif column == 2:
                self.__ptable[0][row].defencepoints = int(value)
            elif column == 3:
                self.__ptable[0][row].keeperpoints = int(value) 
            
            self.__ptable[0][row].calcPlayerpoints()
            return True
        return False
        
    def insertRows(self, position, rows, parent = QtCore.QModelIndex()):
        # Syntax: self.beginInsertRows(index,first,last)
        self.beginInsertRows(parent, position, position + rows - 1)  
        
        for i in range(rows):
            self.__ptable.insert(position, TeamGenerator.Player.Player({'name': 'Neuer Spieler',
                                                          'attackpoints': 0,
                                                          'defencepoints': 0, 
                                                          'keeperpoints': 0}))        
        self.endInsertRows()
        
        
#        return True
        
    def removeRows(self, position, rows, parent = QtCore.QModelIndex()):
        self.beginRemoveRows(parent, position, position + rows - 1)
        
        for i in range(rows):
            value = self.__ptable[position]
            self.__ptable.remove(value)
             
        self.endRemoveRows()
        return True
        
#==============================================================================
#     def sort(self, Ncol, order):
#         """Sort table by given column number.
#         """
#         self.emit(SIGNAL("layoutAboutToBeChanged()"))
#         self.arraydata = sorted(self.arraydata, key=operator.itemgetter(Ncol))        
#         if order == Qt.DescendingOrder:
#             self.arraydata.reverse()
#         self.emit(SIGNAL("layoutChanged()"))
#==============================================================================
        
        


def insertClicked():
    tgm.insertRows(3,1)        

#==============================================================================
# def clicked0():
#     print ('0 clicked')
# def clicked1():
#     print ('1 clicked')
# def clicked2():
#     print ('2 clicked')
# def clicked3():
#     print ('3 clicked')
# def clicked4():
#     print ('4 clicked')
#==============================================================================
    
def tableClick():
    print ('§§§§§§§§§§§§§§§§§§§TABLE CLICKED §§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§')

if __name__ == '__main__':
    
    print('----- START -----')
    
    app = QApplication(sys.argv)
    s1 = loadUi('./.GUI/GUI_Number_1.ui')
    
    s1.show()
    
    
    tg = TeamGenerator.TeamGenerator()
    print('---- Load both teams as they have been the saved to file ----')
    tg.loadTeam('fullTeam','./Input/', 'FullTeam.json')
    
    
    print("########### TEST START ############")
    print(tg.fullTeam.players)    
    print("++++++++++++++++++")
    
    dummy = range(0, len(tg.fullTeam.players))
   
    print("dummy=",dummy)   
    print("########### TEST START ############")    
     
    tgm = TeamGeneratorModel([tg.fullTeam.players,tg.fullTeam.players,tg.fullTeam.players,tg.fullTeam.players,tg.fullTeam.players])#[[tg.fullTeam.players.name], [tg.fullTeam.players.attackpoints], [tg.fullTeam.players.defencepoints]] ) #     ['1', '2', '3'])
    
    s1.tableView_A.setModel(tgm)
    
    s1.pushButton_2.clicked.connect(insertClicked)
#    s1.pushButton_1.clicked.connect(sort2)
#==============================================================================
#     s1.tableView_A.header.connect(s1.tableView_A.header.horizontalHeader(),
#                                   QtCore.SIGNAL('sectionClicked (0)'),
#                                   clicked0)
#     s1.tableView_A.header.connect(s1.tableView_A.header.horizontalHeader(),
#                                   QtCore.SIGNAL('sectionClicked (1)'),
#                                   clicked1)
#     s1.tableView_A.header.connect(s1.tableView_A.header.horizontalHeader(),
#                                   QtCore.SIGNAL('sectionClicked (2)'),
#                                   clicked2)
#     s1.tableView_A.header.connect(s1.tableView_A.header.horizontalHeader(),
#                                   QtCore.SIGNAL('sectionClicked (3)'),
#                                   clicked3)
#     s1.tableView_A.header.connect(s1.tableView_A.header.horizontalHeader(),
#                                   QtCore.SIGNAL('sectionClicked (4)'),
#                                   clicked4)    
#==============================================================================
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    print('----- END -----')
    
    sys.exit(app.exec_())
    
    print('----- STOP -----')