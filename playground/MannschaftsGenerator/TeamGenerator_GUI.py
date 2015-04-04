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
        
#        if self.__ptable[row].available == 0:
#            index.row().setTextColor(QtCore.Qt.red)
        
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

        

        if role == QtCore.Qt.EditRole:
            
            row = index.row()
            column = index.column()
            
#            print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
#            if self.__ptable[row].available == 0:
#                index.row().setTextColor(QtCore.Qt.red)            
            
            if column == 0:
                self.__ptable[row].name = str(value)
            elif column == 1:
                self.__ptable[row].attackpoints = int(value) 
            elif column == 2:
                self.__ptable[row].defencepoints = int(value)
            elif column == 3:
                self.__ptable[row].keeperpoints = int(value) 
            
            self.__ptable[row].calcPlayerpoints()
            s1.gesammt_A.setText("%.2f" % tg.teamA.calcTeampoints())
            s1.angriff_A.setText(str(tg.teamA.attackpoints))
            s1.abwehr_A.setText(str(tg.teamA.defencepoints))
            s1.tor_A.setText(str(tg.teamA.keeperpoints))
            s1.gesammt_B.setText("%.2f" % tg.teamB.calcTeampoints())
            s1.angriff_B.setText(str(tg.teamB.attackpoints))
            s1.abwehr_B.setText(str(tg.teamB.defencepoints))
            s1.tor_B.setText(str(tg.teamB.keeperpoints))
            return True
        s1.gesammt_A.setText("%.2f" % tg.teamA.calcTeampoints())
        s1.gesammt_B.setText("%.2f" % tg.teamB.calcTeampoints())
        return False
        
    def insertRows(self, position, rows, parent = QtCore.QModelIndex()):
        # Syntax: self.beginInsertRows(index,first,last)
        self.beginInsertRows(parent, position, position + rows - 1)  
        newPlayer = TeamGenerator.Player.Player({'name': '<Neuer Spieler>',
                                          'attackpoints': 0,
                                          'defencepoints': 0, 
                                          'keeperpoints': 0,
                                          'available': 0})        
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
    
    currentTable = getCurrentPlayer()[1]
    if currentTable == 'A':    
        tgmA.insertRows(0,1)
    elif currentTable == 'B':
        tgmB.insertRows(0,1)        
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


#def refreshGUI():
#    tgmA.dataChanged.emit()        
#    tgmB.dataChanged.emit()
    
def refreshGUI(seite = 2):
    if seite == 2:
        s1.gesammt_A.setText("%.2f" % tg.teamA.calcTeampoints())
        s1.angriff_A.setText(str(tg.teamA.attackpoints))
        s1.abwehr_A.setText(str(tg.teamA.defencepoints))
        s1.tor_A.setText(str(tg.teamA.keeperpoints))
        s1.gesammt_B.setText("%.2f" % tg.teamB.calcTeampoints())
        s1.angriff_B.setText(str(tg.teamB.attackpoints))
        s1.abwehr_B.setText(str(tg.teamB.defencepoints))
        s1.tor_B.setText(str(tg.teamB.keeperpoints))
        
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
    
    elif seite == 1:
        tgmA = TeamGeneratorModel(tg.teamA.players)
        tgmF = TeamGeneratorModel(tg.fullTeam.players)
        
        proxyA = PlayerFilterProxyModel(tgmA)
        proxyA.setSourceModel(tgmA)
        proxyF = PlayerFilterProxyModel(tgmF)
        proxyF.setSourceModel(tgmF)
        
        werSp.allView.setModel(proxyF)
        werSp.aView.setModel(proxyA)
        

def getCurrentPlayer():
    print("getCurrentPlayer")    
    
    selModelA = s1.tableView_A.selectionModel()
    selModelB = s1.tableView_B.selectionModel()
    
    indexes = selModelA.selectedIndexes()
    if (indexes != [] ):
        indexes = selModelA.selectedIndexes()
        return [indexes, 'A']
#        for index in indexes:
#            text = u"(%i,%i)" % (index.row(), index.column())
#            print(text)
#            return [index, "A"]
    else:
        indexes = selModelB.selectedIndexes()
        if (indexes != [] ):
            indexes = selModelB.selectedIndexes()
            return [indexes, 'B']
                   
    return [[], 'x']
    
def switch():
    indexes = getCurrentPlayer()
#    x_sauber = list(set(x))
    selectetPlayers = []
    
    for index in(indexes[0]):
        selectetPlayers.append(int(index.row()))
    
    selectetPlayers = list(set(selectetPlayers))
    selectetPlayers.sort(reverse = True)
        
    if indexes[1] == 'A':
        for i in selectetPlayers:
            tg.teamB.addPlayer(tg.teamA.removeByIndex(i))
        
    elif indexes[1] == 'B':
        for i in selectetPlayers:
            tg.teamA.addPlayer(tg.teamB.removeByIndex(i))
    else:
        pass
    
    refreshGUI()
    
def removeFromTable():
    indexes = getCurrentPlayer()
    selectetPlayers = []
    
    for index in(indexes[0]):
        selectetPlayers.append(int(index.row()))
    
    selectetPlayers = list(set(selectetPlayers))
    selectetPlayers.sort(reverse = True)
        
    if indexes[1] == 'A':
        for i in selectetPlayers:
            tg.teamA.removeByIndex(i)
        
    elif indexes[1] == 'B':
        for i in selectetPlayers:
            tg.teamB.removeByIndex(i)
    else:
        pass
    
    refreshGUI()
    
def weiter():
    werSp.close()
    warte.show()
    callBerechneManschaften()
    s1.show()
    warte.close()
    
def spieltMit():
    print ('spieltMit')
    selModelF = werSp.allView.selectionModel()
    selModelA = werSp.aView.selectionModel()
    
    indexes = selModelA.selectedIndexes()
    if (indexes != [] ):
        indexes = selModelA.selectedIndexes()
        for index in reversed(indexes):
            tg.fullTeam.addPlayer(tg.teamA.removeByIndex(index.row()))

    else:
        indexes = selModelF.selectedIndexes()
        if (indexes != [] ):
            indexes = selModelF.selectedIndexes()
            for index in reversed(indexes):
                tg.teamA.addPlayer(tg.fullTeam.removeByIndex(index.row()))
    refreshGUI(1)
            
def oeffnen():
    print ('öffnen clicked')
    winOpen.show()
    winOpen.Btn.clicked.connect(oeffnen2)

def oeffnen2():  
    tg.loadTeam('fullTeam','./Input/', winOpen.eingabe.displayText())
    refreshGUI(1)
    
def speichern():
    print('speichern')
    winSave.show()
    winSave.Btn.clicked.connect(speichern2)
    
def speichern2():
    tg.dumpTeam('fullTeam','./Input/', winSave.eingabe.displayText())
    refreshGUI(1)
    
def werSpAdd():
    tgmF.insertRows(0,1)
    refreshGUI(1)
    
def werSpRemove():
    selModelF = werSp.allView.selectionModel()
    selModelA = werSp.aView.selectionModel()
    
    indexes = selModelA.selectedIndexes()
    if (indexes != [] ):
        indexes = selModelA.selectedIndexes()
        for index in reversed(indexes):
            tg.teamA.removeByIndex(index.row())

    else:
        indexes = selModelF.selectedIndexes()
        if (indexes != [] ):
            indexes = selModelF.selectedIndexes()
            for index in reversed(indexes):
                tg.fullTeam.removeByIndex(index.row())
    refreshGUI(1)
    
def wilWeiter():
    werSp.show()
    willcome.close()
    
    
            
    
if __name__ == '__main__':
  
 
   
    
    print('----- START -----')
    
    app = QApplication(sys.argv)
    s1 = loadUi('./.GUI/GUI_Number_1.ui')
    werSp = loadUi('./.GUI/werSpielt.ui')
    warte = loadUi('./.GUI/warte.ui')
    winOpen = loadUi('./.GUI/oeffnen.ui')
    winSave = loadUi('./.GUI/speichern.ui')
    willcome = loadUi('./.GUI/Oberfläche.ui')
        
    willcome.show()
    willcome.startWeiterBtn.clicked.connect(wilWeiter)
    werSp.weiter_Btn.clicked.connect(weiter)
    werSp.actionOeffnen.triggered.connect(oeffnen)
    werSp.actionSpeichern.triggered.connect(speichern)
    
    tg = TeamGenerator.TeamGenerator()
    print('---- Load both teams as they have been the saved to file ----')
#    tg.loadTeam('teamA','./Input/', 'SmallTeam.json')


    print("########### TEAM A: ############")
    tg.teamA.print()
    print("########### TEAM B: ############")
    tg.teamB.print()
    
    print("########### TEST START ############")
    #print(str(p.name) for p in tg.fullTeam.players)    
    #print("++++++++++++++++++")
    
    ##########################################################################
    # Data[tg.teamA.players] ---> DataModel[tgmA] 
    tgmF = TeamGeneratorModel(tg.fullTeam.players)
#    tgmF.insertRows(0,5)  
#    print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&')
    
    tgmA = TeamGeneratorModel(tg.teamA.players)#[[tg.fullTeam.players.name], [tg.fullTeam.players.attackpoints], [tg.fullTeam.players.defencepoints]] ) #     ['1', '2', '3'])
    tgmB = TeamGeneratorModel(tg.teamB.players)
    
    # DataModel[tgmA]  ---> ProxyModel[proxyA]
    proxyA = PlayerFilterProxyModel(tgmA)
    proxyA.setSourceModel(tgmA)
    proxyB = PlayerFilterProxyModel(tgmB)
    proxyB.setSourceModel(tgmB) 
    proxyF = PlayerFilterProxyModel(tgmF)
    proxyF.setSourceModel(tgmF)
  
    # ProxyModel[proxyA]--->ViewModel[tableView_A]
    s1.tableView_A.setModel(proxyA)  
    s1.tableView_B.setModel(proxyB)
    werSp.allView.setModel(proxyF)
    werSp.aView.setModel(proxyA)
    ##########################################################################
 



    # QtCore.QObject.connect(self.uiTree.selectionModel(),
    #           QtCore.SIGNAL("currentChanged(QModelIndex, QModelIndex)"),
    #                                       self._propEditor.setSelection)





    s1.pushButton_3.clicked.connect(removeFromTable)
    s1.pushButton_2.clicked.connect(insertClicked)
    s1.pushButton_1.clicked.connect(callBerechneManschaften)
    werSp.add_Btn.clicked.connect(werSpAdd)
    werSp.remove_Btn.clicked.connect(werSpRemove)
    

    s1.gesammt_A.setText("%.2f" % tg.teamA.calcTeampoints())
    s1.angriff_A.setText(str(tg.teamA.attackpoints))
    s1.abwehr_A.setText(str(tg.teamA.defencepoints))
    s1.tor_A.setText(str(tg.teamA.keeperpoints))
    s1.gesammt_B.setText("%.2f" % tg.teamB.calcTeampoints())
    s1.angriff_B.setText(str(tg.teamB.attackpoints))
    s1.abwehr_B.setText(str(tg.teamB.defencepoints))
    s1.tor_B.setText(str(tg.teamB.keeperpoints))
    
    
    s1.pushButton.clicked.connect(switch)
    print('----- END -----')
    
    selModelA = s1.tableView_A.selectionModel()
    selModelB = s1.tableView_B.selectionModel()
    
    werSp.jaNein_Btn.clicked.connect(spieltMit)
    
    sys.exit(app.exec_())
    
    print('----- STOP -----')