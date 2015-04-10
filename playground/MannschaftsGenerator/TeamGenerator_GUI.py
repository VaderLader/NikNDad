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
         self.__ptable = sorted(self.__ptable, key=QtCore.operator.itemgetter(Ncol))        
         if order == QtCore.Qt.DescendingOrder:
             self.arraydata.reverse()
         self.emit(QtCore.SIGNAL("layoutChanged()"))

#==============================================================================

#==============================================================================
class PlayerFilterProxyModel(QtGui.QSortFilterProxyModel):
    ''' Just inherited from the base class as it is
    '''
    pass
#==============================================================================       

class welcomeWind:
    def __init__(self):
        welcomeWindow.startWeiterBtn.clicked.connect(lambda: self.welcomeDone())
        welcomeWindow.show()
    
    def welcomeDone(self):
        tg.loadTeam('fullTeam','./Input/','FullTeam.json')    
        playerSelectWindow.show()
        pswin.refreshGUI()
        welcomeWindow.close()
    


#==============================================================================
class calculateTeamWind:
    def __init__(self):
        calculatedTeamWindow.pushButton_2.clicked.connect(lambda: self.insertClicked())
        calculatedTeamWindow.pushButton_1.clicked.connect(lambda: self.callBerechneManschaften())
        calculatedTeamWindow.pushButton.clicked.connect(lambda: self.shiftPlayer())
        calculatedTeamWindow.pushButton_3.clicked.connect(lambda: self.removeFromTable())
        calculatedTeamWindow.actionSpeichern.triggered.connect(lambda: self.save())
        calculatedTeamWindow.actionSpeichern_unter.triggered.connect(lambda: self.saveAsDia())
        self.refreshGUI()
    

    def getSelectedPlayers(self):
        ''' Get the list currently selected indexes + table name
        
        :returns: [ [List of selected players], 'TableName' ]
        :rtype: [ [], str]
        '''
        print("getSelectedPlayers")    
        
        selModelA = calculatedTeamWindow.tableView_A.selectionModel()
        selModelB = calculatedTeamWindow.tableView_B.selectionModel()
        
        indexes = selModelA.selectedIndexes()
        if (indexes != [] ):
            indexes = selModelA.selectedIndexes()
            return [indexes, 'teamA']
        else:
            indexes = selModelB.selectedIndexes()
            if (indexes != [] ):
                indexes = selModelB.selectedIndexes()
                return [indexes, 'teamB']
                       
        return [[], '']
    
    
    def insertClicked(self):
        '''Dependent on the focus one row on Table A or Table B is inserted'''
        
        currentTable = self.getSelectedPlayers()[1]
        if currentTable == 'A':    
            tgmA.insertRows(0,1)
        elif currentTable == 'B':
            tgmB.insertRows(0,1)             
        self.refreshGUI()

    def callBerechneManschaften(self):
        #TODO: Shift all to teamA ....
        print("### callBerechneManschaften() ###")
        tg.berechneMannschaften()    
        print("########### TEAM A: ############")
        tg.teamA.print()
        print("########### TEAM B: ############")
        tg.teamB.print()
        self.refreshGUI()    
    
    def shiftPlayer(self):
        indexes = self.getSelectedPlayers()
        selectedPlayers = []
        
        #: Building a list of Players in reverse order to be shifted
        #: The selectedPlayers list can contain players several times depending on what
        #: was selected. => set(selectedPlayers) has only unique Players
        for index in(indexes[0]):
            selectedPlayers.append(int(index.row()))
        
        selectedPlayers = list(set(selectedPlayers))
        selectedPlayers.sort(reverse = True)
            
        if indexes[1] == 'teamA':
            for i in selectedPlayers:
                tg.teamB.addPlayer(tg.teamA.removeByIndex(i))
            
        elif indexes[1] == 'teamB':
            for i in selectedPlayers:
                tg.teamA.addPlayer(tg.teamB.removeByIndex(i))
        else:
            pass
        
        self.refreshGUI()   
    
    def removeFromTable(self):
        indexes = self.getSelectedPlayers()
        selectetPlayers = []
        
        for index in(indexes[0]):
            selectetPlayers.append(int(index.row()))
            
        #: set() liste of unique elements
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
        
        self.refreshGUI()

    def save(self):
        print('Speichern in default directory')
        #savedir = QtGui.QFileDialog.getExistingDirectory(QtGui.QWidget(),'','./Results')
        # getSaveFileName(QtGui.QWidget(), 'Speichere beide Teams','./Result/','*.json')
        tg.dumpTeams('./Result/')
        self.refreshGUI()
        
    def saveAsDia(self):
        ''' Save both Team with save dialog window '''
        filename = QtGui.QFileDialog.getSaveFileName(QtGui.QWidget(), 'Speichere TeamA','./Result/','*.json')
        tg.dumpTeam('teamA','', filename)
        filename = QtGui.QFileDialog.getSaveFileName(QtGui.QWidget(), 'Speichere TeamB','./Result/','*.json')
        tg.dumpTeam('teamB','', filename)
        self.refreshGUI()        
        
        
    def refreshGUI(self):
        ''' method to refresh all displayed data '''
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
        
#==============================================================================    
class playerSelectWind:
    
    def __init__(self):
        playerSelectWindow.add_Btn.clicked.connect(lambda: self.playerSelectWindowAdd())
        playerSelectWindow.remove_Btn.clicked.connect(lambda: self.playerSelectWindowRemove())
        playerSelectWindow.jaNein_Btn.clicked.connect(lambda: self.shiftPlayer())
        playerSelectWindow.weiter_Btn.clicked.connect(lambda: self.gotoNextWindow())
        playerSelectWindow.actionOpen.triggered.connect(lambda: self.openDia())
        playerSelectWindow.actionSave.triggered.connect(lambda: self.saveDia())    
        self.refreshGUI()

    def openDia(self):
        print ('öffnen clicked')
        #playerSelectWindow
        filename = QtGui.QFileDialog.getOpenFileName(QtGui.QWidget(), 'Lade eine Spielerliste oder ein Team','./Input/','*.json')
       # file=open(filename)
        tg.loadTeam('fullTeam','',filename)    
        self.refreshGUI()
                  
    def saveDia(self):
        print('speichern')
        filename = QtGui.QFileDialog.getSaveFileName(QtGui.QWidget(), 'Speichere eine Spielerliste oder ein Team','./Input/','*.json')
        tg.dumpTeam('fullTeam','', filename)
        self.refreshGUI()
      
    def callBerechneManschaften(self):
        print("### callBerechneManschaften() ###")
        tg.berechneMannschaften()    
        print("########### TEAM A: ############")
        tg.teamA.print()
        print("########### TEAM B: ############")
        tg.teamB.print()
        self.refreshGUI()        
    
    def gotoNextWindow(self):
        #TODO: ggggg
        playerSelectWindow.close()
       # waitingCalculation.show()
        print("gotoNextWindow1")
        waitingCalculation.textBrowser.setText("Hallo")
        waitingCalculation.show()
                
        #self.callBerechneManschaften()
        print("gotoNextWindow2")
        calculatedTeamWindow.show()
        ctwin.refreshGUI()
        #waitingCalculation.close()

    def getSelectedPlayers(self):
        ''' Get the list currently selected indexes + table name
        
        :returns: [ [List of selected players], 'TableName' ]
        :rtype: [ [], str]
        '''
        print("getSelectedPlayers")    
        
        selModelF = playerSelectWindow.fullView.selectionModel()
        selModelA = playerSelectWindow.aView.selectionModel()
        
        
        indexes = selModelF.selectedIndexes()
        if (indexes != [] ):
            indexes = selModelF.selectedIndexes()
            return [indexes, 'fullTeam']
        else:
            indexes = selModelA.selectedIndexes()
            if (indexes != [] ):
                indexes = selModelA.selectedIndexes()
                return [indexes, 'teamA']
                       
        return [[], ''] 
 
 
    def shiftPlayer(self):
        indexes = self.getSelectedPlayers()
        selectedPlayers = []
        
        #: Building a list of Players in reverse order to be shifted
        #: The selectedPlayers list can contain players several times depending on what
        #: was selected. => set(selectedPlayers) has only unique Players
        for index in indexes[0]:
            selectedPlayers.append(int(index.row()))
        
        selectedPlayers = list(set(selectedPlayers))
        selectedPlayers.sort(reverse = True)
            
        if indexes[1] == 'fullTeam':
            for i in selectedPlayers:
                tg.teamA.addPlayer(tg.fullTeam.removeByIndex(i))
            
        elif indexes[1] == 'teamA':
            for i in selectedPlayers:
                tg.fullTeam.addPlayer(tg.teamA.removeByIndex(i))
        else:
            pass
        
        self.refreshGUI()  

     
    def playerSelectWindowAdd(self):
        tgmF.insertRows(0,1)
        self.refreshGUI()
        
    def playerSelectWindowRemove(self):
        selModelF = playerSelectWindow.fullView.selectionModel()
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
        self.refreshGUI()

     
    def refreshGUI(self):
        tgmA = TeamGeneratorModel(tg.teamA.players)
        tgmF = TeamGeneratorModel(tg.fullTeam.players)
        
        proxyA = PlayerFilterProxyModel(tgmA)
        proxyA.setSourceModel(tgmA)
        proxyF = PlayerFilterProxyModel(tgmF)
        proxyF.setSourceModel(tgmF)
        
        playerSelectWindow.fullView.setModel(proxyF)
        playerSelectWindow.aView.setModel(proxyA)
            

#===================================================================================================
class waitingCalculationWind:
    def __init__(self):
        waitingCalculation.textBrowser.setText("Hallo")
        pass
#===================================================================================================
    
    
    
if __name__ == '__main__':
    print('----- START of TeamGenerator_GUI -----')
    
    #: Data[tg.teamA.players] ---> DataModel[tgmA] 
    #: DataModel[tgmA]  ---> ProxyModel[proxyA]
    #: ProxyModel[proxyA]--->ViewModel[tableView_A]
       
    
    tg = TeamGenerator.TeamGenerator()
    print('---- Load both teams as they have been the saved to file ----')
    #    tg.loadTeam('teamA','./Input/', 'SmallTeam.json')
    
    
    #print("########### TEAM A: ############")
    #print(tg.teamA.print())
    #print("########### TEAM B: ############")
    #print(tg.teamB.print())
    
    ##########################################################################
    #: Data[tg.teamA.players] ---> DataModel[tgmA] 
    tgmF = TeamGeneratorModel(tg.fullTeam.players)
    
    tgmA = TeamGeneratorModel(tg.teamA.players)#[[tg.fullTeam.players.name], [tg.fullTeam.players.attackpoints], [tg.fullTeam.players.defencepoints]] ) #     ['1', '2', '3'])
    tgmB = TeamGeneratorModel(tg.teamB.players)
    
    
    #:
    app = QtGui.QApplication(sys.argv)
    
    welcomeWindow =         uic.loadUi('./.GUI/welcomeWindow.ui')
    playerSelectWindow =    uic.loadUi('./.GUI/playerSelectWindow.ui')     
    calculatedTeamWindow =  uic.loadUi('./.GUI/calculatedTeamWindow.ui')   
    waitingCalculation =    uic.loadUi('./.GUI/waitingCalculation.ui')

    wcwin = welcomeWind()
    ctwin = calculateTeamWind()
    pswin = playerSelectWind()
    waitwin = waitingCalculationWind() 
    
    #:Showing the first window. All the next windows are
    #:called from the windows before. 
    welcomeWindow.show()
    print('GUI up and running now ')
     
    app.exec_()
    print('----- END of TeamGenerator_GUI -----')