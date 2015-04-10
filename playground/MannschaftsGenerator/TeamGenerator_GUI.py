# -*- coding: utf-8 -*-
"""
Created on Sat Feb 28 16:43:55 2015

@author: pi
"""

import sys
import PyQt4.QtCore as QtCore
import PyQt4.QtGui as QtGui
#from PyQt4.QtGui import *
#from PyQt4.uic import *
import PyQt4.uic as uic 

import TeamGenerator

#==============================================================================
class TeamGeneratorModel(QtCore.QAbstractTableModel):

    def __init__(self, ptable = [], parent = None):
        QtCore.QAbstractTableModel.__init__(self, parent)
        self.__ptable = ptable
        
      
    def headerData(self, section, orientation, role):
        ''' Set fixed column header'''
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
                    return 'Gesamt'        
            else:                
                return "Spieler " + str(section)  
    
    def data(self, index, role):
        ''' Return data from __ptable
        
        :param index: index
        :type index: QModelIndex
        :param role: role
        :type role: QtCore.Qt.DisplayRole
        :returns: Table Cell Value
        :rtype: str/int/float
        
        '''
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
        ''' Number of rows in the table '''
        return len(self.__ptable)
        
    def columnCount(self, parent):
        ''' Fixed number of columns = 5 '''
        return 5
    
    def flags(self,index):
        ''' Controls if item is enabled; editable and selectable
        '''
        return QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable
        
    def setData(self, index, value, role = QtCore.Qt.EditRole):
        ''' This method is always called if data has to be displayed in the GUI
        
        :param index: index
        :type index:
        :param value: value of the cell
        :type vale:
        :returns: True/False
        :rtype: bool
        '''
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
            calculatedTeamWindow.gesammt_A.setText("%.2f" % tg.teamA.calcTeampoints())
            calculatedTeamWindow.angriff_A.setText(str(tg.teamA.attackpoints))
            calculatedTeamWindow.abwehr_A.setText(str(tg.teamA.defencepoints))
            calculatedTeamWindow.tor_A.setText(str(tg.teamA.keeperpoints))
            calculatedTeamWindow.gesammt_B.setText("%.2f" % tg.teamB.calcTeampoints())
            calculatedTeamWindow.angriff_B.setText(str(tg.teamB.attackpoints))
            calculatedTeamWindow.abwehr_B.setText(str(tg.teamB.defencepoints))
            calculatedTeamWindow.tor_B.setText(str(tg.teamB.keeperpoints))
            return True
        
        calculatedTeamWindow.gesammt_A.setText("%.2f" % tg.teamA.calcTeampoints())
        calculatedTeamWindow.gesammt_B.setText("%.2f" % tg.teamB.calcTeampoints())
        return False
        
    def insertRows(self, position, rows, parent = QtCore.QModelIndex()):
        ''' Insert rows at position
            
        '''        
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
        """Removes rows from the table 

        :param position: Number of the first row, which is removed
        :type positionn: int 
        :param rows: Number of rows to be removed
        :type rows: int 
        :returns: True
        :rtype: bool
        """
       
        self.beginRemoveRows(parent, position, position + rows - 1)
        
        for i in range(rows):
            value = self.__ptable[position]
            self.__ptable.remove(value)
             
        self.endRemoveRows()
        return True

    
    def sort(self, Ncol, order):
         """Sort table by given column number.
         """
         #self.emit(SIGNAL("layoutAboutToBeChanged()"))
         self.__ptable = sorted(self.__ptable, key=operator.itemgetter(Ncol))        
         if order == Qt.DescendingOrder:
             self.arraydata.reverse()
         self.emit(SIGNAL("layoutChanged()"))

#==============================================================================

#==============================================================================
class PlayerFilterProxyModel(QtGui.QSortFilterProxyModel):
    ''' Just inherited from the base class as it is
    '''
    pass
#==============================================================================       



#==============================================================================
def insertClicked():
    '''Dependent on the focus one row on Table A or Table B is inserted'''
    
    currentTable = getCurrentPlayer()[1]
    if currentTable == 'A':    
        tgmA.insertRows(0,1)
    elif currentTable == 'B':
        tgmB.insertRows(0,1)             
    refreshGUI()    

    
def callBerechneManschaften():
    print("### callBerechneManschaften() ###")
    tg.berechneMannschaften()    
    print("########### TEAM A: ############")
    tg.teamA.print()
    print("########### TEAM B: ############")
    tg.teamB.print()
    refreshGUI()    

    
def refreshGUI(window = 2):
    ''' method to refresh all displayed data '''
    if window == 2:
        calculatedTeamWindow.gesammt_A.setText("%.2f" % tg.teamA.calcTeampoints())
        calculatedTeamWindow.angriff_A.setText(str(tg.teamA.attackpoints))
        calculatedTeamWindow.abwehr_A.setText(str(tg.teamA.defencepoints))
        calculatedTeamWindow.tor_A.setText(str(tg.teamA.keeperpoints))
        calculatedTeamWindow.gesammt_B.setText("%.2f" % tg.teamB.calcTeampoints())
        calculatedTeamWindow.angriff_B.setText(str(tg.teamB.attackpoints))
        calculatedTeamWindow.abwehr_B.setText(str(tg.teamB.defencepoints))
        calculatedTeamWindow.tor_B.setText(str(tg.teamB.keeperpoints))
        
        tgmA = TeamGeneratorModel(tg.teamA.players)
        tgmB = TeamGeneratorModel(tg.teamB.players)
        calculatedTeamWindow.tableView_A.setModel(tgmA)
        calculatedTeamWindow.tableView_B.setModel(tgmB)
            
    
        proxyA = PlayerFilterProxyModel(tgmA)
        proxyA.setSourceModel(tgmA)
        calculatedTeamWindow.tableView_A.setModel(proxyA)  
        
        proxyB = PlayerFilterProxyModel(tgmB)
        proxyB.setSourceModel(tgmB) 
        calculatedTeamWindow.tableView_B.setModel(proxyB)
    
    elif window == 1:
        tgmA = TeamGeneratorModel(tg.teamA.players)
        tgmF = TeamGeneratorModel(tg.fullTeam.players)
        
        proxyA = PlayerFilterProxyModel(tgmA)
        proxyA.setSourceModel(tgmA)
        proxyF = PlayerFilterProxyModel(tgmF)
        proxyF.setSourceModel(tgmF)
        
        playerSelectWindow.allView.setModel(proxyF)
        playerSelectWindow.aView.setModel(proxyA)
        

def getCurrentPlayer():
    print("getCurrentPlayer")    
    
    selModelA = calculatedTeamWindow.tableView_A.selectionModel()
    selModelB = calculatedTeamWindow.tableView_B.selectionModel()
    
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
    playerSelectWindow.close()
    waitingCalculation.show()
    callBerechneManschaften()
    calculatedTeamWindow.show()
    waitingCalculation.close()
    
def spieltMit():
    print ('spieltMit')
    selModelF = playerSelectWindow.allView.selectionModel()
    selModelA = playerSelectWindow.aView.selectionModel()
    
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
    #playerSelectWindow
    filename = QtGui.QFileDialog.getOpenFileName(QtGui.QWidget(), 'Lade ein Team','./Input/','*.json')
   # file=open(filename)
    tg.loadTeam('fullTeam','',filename)    
    refreshGUI(1)
        
    #data = file.read()
    #playerSelectWindow.textEdit.setText(data)
        
    
    #winOpen.show()
    
    #winOpen.Btn.clicked.connect(oeffnen2)

#def oeffnen2():  
 #tg.loadTeam('fullTeam','./Input/', winOpen.eingabe.displayText())
 #refreshGUI(1)
    
def speichern():
    print('speichern')
    filename = QtGui.QFileDialog.getSaveFileName(QtGui.QWidget(), 'Speichere ein Team','./Input/','*.json')
    tg.dumpTeam('fullTeam','', filename)
    refreshGUI(1)
    
  # winSave.show()
    #winSave.Btn.clicked.connect(speichern2)
    
#def speichern2():
#    tg.dumpTeam('fullTeam','./Input/', winSave.eingabe.displayText())
#    refreshGUI(1)
    
def playerSelectWindowAdd():
    tgmF.insertRows(0,1)
    refreshGUI(1)
    
def playerSelectWindowRemove():
    selModelF = playerSelectWindow.allView.selectionModel()
    selModelA = playerSelectWindow.aView.selectionModel()
    
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
    
def willWeiter():
    playerSelectWindow.show()
    welcomeWindow.close()
    
    
            
    
if __name__ == '__main__':
  
   
    
    print('----- START -----')
    
    app = QtGui.QApplication(sys.argv)
    calculatedTeamWindow =   uic.loadUi('./.GUI/calculatedTeamWindow.ui')
    playerSelectWindow =     uic.loadUi('./.GUI/playerSelectWindow.ui')
    waitingCalculation =     uic.loadUi('./.GUI/waitingCalculation.ui')
    welcomeWindow =   uic.loadUi('./.GUI/welcomeWindow.ui')
        
    welcomeWindow.show()
    welcomeWindow.startWeiterBtn.clicked.connect(willWeiter)
    playerSelectWindow.weiter_Btn.clicked.connect(weiter)
    playerSelectWindow.actionOeffnen.triggered.connect(oeffnen)
    playerSelectWindow.actionSpeichern.triggered.connect(speichern)
    
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
    calculatedTeamWindow.tableView_A.setModel(proxyA)  
    calculatedTeamWindow.tableView_B.setModel(proxyB)
    playerSelectWindow.allView.setModel(proxyF)
    playerSelectWindow.aView.setModel(proxyA)
    ##########################################################################
 



    # QtCore.QObject.connect(self.uiTree.selectionModel(),
    #           QtCore.SIGNAL("currentChanged(QModelIndex, QModelIndex)"),
    #                                       self._propEditor.setSelection)





    calculatedTeamWindow.pushButton_3.clicked.connect(removeFromTable)
    calculatedTeamWindow.pushButton_2.clicked.connect(insertClicked)
    calculatedTeamWindow.pushButton_1.clicked.connect(callBerechneManschaften)
    playerSelectWindow.add_Btn.clicked.connect(playerSelectWindowAdd)
    playerSelectWindow.remove_Btn.clicked.connect(playerSelectWindowRemove)
    

    calculatedTeamWindow.gesammt_A.setText("%.2f" % tg.teamA.calcTeampoints())
    calculatedTeamWindow.angriff_A.setText(str(tg.teamA.attackpoints))
    calculatedTeamWindow.abwehr_A.setText(str(tg.teamA.defencepoints))
    calculatedTeamWindow.tor_A.setText(str(tg.teamA.keeperpoints))
    calculatedTeamWindow.gesammt_B.setText("%.2f" % tg.teamB.calcTeampoints())
    calculatedTeamWindow.angriff_B.setText(str(tg.teamB.attackpoints))
    calculatedTeamWindow.abwehr_B.setText(str(tg.teamB.defencepoints))
    calculatedTeamWindow.tor_B.setText(str(tg.teamB.keeperpoints))
    
    
    calculatedTeamWindow.pushButton.clicked.connect(switch)
    print('----- END -----')
    
    selModelA = calculatedTeamWindow.tableView_A.selectionModel()
    selModelB = calculatedTeamWindow.tableView_B.selectionModel()
    
    playerSelectWindow.jaNein_Btn.clicked.connect(spieltMit)
    
    sys.exit(app.exec_())
    
    print('----- STOP -----')