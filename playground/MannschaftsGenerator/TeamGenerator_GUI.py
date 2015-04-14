# -*- coding: utf-8 -*-
"""
Created on Sat Feb 28 16:43:55 2015

@author: SohnyBohny
"""

import sys
import PyQt4.QtCore as QtCore
import PyQt4.QtGui as QtGui
#from PyQt4.QtGui import *
#from PyQt4.uic import *
import PyQt4.uic as uic 

import TeamGenerator

#===================================================================================================
class TeamGeneratorModel(QtCore.QAbstractTableModel):

    def __init__(self, ptable = [], parent = None):
        QtCore.QAbstractTableModel.__init__(self, parent)
        self.__ptable = ptable
        print("TeamGeneratorModel.__init__: len(__ptable)=", len(self.__ptable))
        
    def get_ptable(self):
        return self.__ptable

    def ptableUpdate(self, ptable = []):
        self.__ptable = ptable
        
    def headerData(self, section, orientation, role):
        ''' Defines the fixed column header
        
        :param section:
        :type section: 
        :param orientation:
        :type orientation: QtCore.Qt
        :returns: Header - this is th title of each column
        :rtype: str
        '''
        
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
#            calculatedTeamWindow.gesammt_A.setText("%.2f" % tg.teamA.calcTeampoints())
#            calculatedTeamWindow.angriff_A.setText(str(tg.teamA.attackpoints))
#            calculatedTeamWindow.abwehr_A.setText(str(tg.teamA.defencepoints))
#            calculatedTeamWindow.tor_A.setText(str(tg.teamA.keeperpoints))
#            calculatedTeamWindow.gesammt_B.setText("%.2f" % tg.teamB.calcTeampoints())
#            calculatedTeamWindow.angriff_B.setText(str(tg.teamB.attackpoints))
#            calculatedTeamWindow.abwehr_B.setText(str(tg.teamB.defencepoints))
#            calculatedTeamWindow.tor_B.setText(str(tg.teamB.keeperpoints))
            print('TeamGeneratorModel.setData() going to emit the signal')            
            self.dataChanged.emit(index, index)
            return True
        
#        calculatedTeamWindow.gesammt_A.setText("%.2f" % tg.teamA.calcTeampoints())
#        calculatedTeamWindow.gesammt_B.setText("%.2f" % tg.teamB.calcTeampoints())
        return False
        
    def insertRows(self, position, rows, parent = QtCore.QModelIndex()):
        ''' Insert rows at position
        :param position: Number of the first row, which is inserted
        :type position: int 
        :param rows: Number of rows to be inserted
        :type rows: int 
        :returns: True
        :rtype: bool
        '''
        print('position = ', position, "rows = ", rows)      
        # Syntax: self.beginInsertRows(index,first,last)
        self.beginInsertRows(parent, position, position + rows - 1)  
        newPlayer = TeamGenerator.Player.Player({'name': '<Neuer Spieler>',
                                          'attackpoints': 0,
                                          'defencepoints': 0, 
                                          'keeperpoints': 0,
                                          'available': 0})
        print("len(self.__ptable)=", len(self.__ptable))                                  
        self.__ptable.insert(position,newPlayer)
        print("len(self.__ptable)=", len(self.__ptable))                                  
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

#===================================================================================================
#===================================================================================================
class PlayerFilterProxyModel(QtGui.QSortFilterProxyModel):
    ''' Just inherited from the base class as it is
    '''
    pass
#===================================================================================================       

class welcomeWind:
    def __init__(self):
        welcomeWindow.startWeiterBtn.clicked.connect(lambda: self.welcomeDone())
        welcomeWindow.show()
    
    def welcomeDone(self):
        print("\n### welcomeDone ###")
        print(" len(tgmF.get_ptable())=",len(tgmF.get_ptable()))
        print(" len(tg.fullTeam.players)=",len(tg.fullTeam.players))
        print(" len(tgmA.get_ptable())=",len(tgmA.get_ptable()))
        print(" len(tg.teamA.players)=",len(tg.teamA.players))
        tg.loadTeam('fullTeam','./Input/','FullTeam.json')    
        print("\n### welcomeDone after loadTeam ###")
        print(" len(tgmF.get_ptable())=",len(tgmF.get_ptable()))
        print(" len(tg.fullTeam.players)=",len(tg.fullTeam.players))
        print(" len(tgmA.get_ptable())=",len(tgmA.get_ptable()))
        print(" len(tg.teamA.players)=",len(tg.teamA.players))
        pswin.refreshGUI()
                
        playerSelectWindow.show()
                
        print("\n### welcomeDone after RefreshGUI ###")
        print(" len(tgmF.get_ptable())=",len(tgmF.get_ptable()))
        print(" len(tg.fullTeam.players)=",len(tg.fullTeam.players))
        print(" len(tgmA.get_ptable())=",len(tgmA.get_ptable()))
        print(" len(tg.teamA.players)=",len(tg.teamA.players))        
        welcomeWindow.close()
    


#===================================================================================================
class calculateTeamWind:
    def __init__(self, tgModelA, tgModelB):
        ''' The two model parameters are needed to connect to the signals from these models
        
        :param tgModelA: Model representing the one Team
        :type tgModelA: TeamGeneratorModel
        :param tgModelB: Model representing the one Team
        :type tgModelB: TeamGeneratorModel
        '''
        self.tgModelA = tgModelA
        self.tgModelB = tgModelB
        self.tgModelA.dataChanged.connect(lambda: self.signalReceived())
        self.tgModelB.dataChanged.connect(lambda: self.signalReceived())
        calculatedTeamWindow.pushButton_2.clicked.connect(lambda: self.addPlayer())
        calculatedTeamWindow.pushButton_1.clicked.connect(lambda: self.callBerechneManschaften())
        calculatedTeamWindow.pushButton.clicked.connect(lambda: self.shiftPlayer())
        calculatedTeamWindow.pushButton_3.clicked.connect(lambda: self.removeFromTable())
        calculatedTeamWindow.actionSpeichern.triggered.connect(lambda: self.save())
        calculatedTeamWindow.actionSpeichern_unter.triggered.connect(lambda: self.saveAsDia())
        calculatedTeamWindow.actionPrint_to_txt.triggered.connect(lambda: self.printTxt())
        self.refreshGUI()
    
    def signalReceived(self):
        print("calculateTeamWind.signalReceived(): received signal")
        self.updateTextBoxes()
        
    def printTxt(self):
        print('print to txt')
        filename = QtGui.QFileDialog.getSaveFileName(QtGui.QWidget(), 'print to *txt','./Result/','*.txt')
        file = open(filename, "w")
        print(filename)

        file.write("Nach langem rechnen haben wir die besten Manschaften zusammengestellt:\n\n")

        file.write(str(tg.teamA.print()+'\n\n'))
        file.write(str(tg.teamB.print()+'\n\n'))
        
        file.write('Viel Spaß beim kicken und bis zum nächsten Mal\nDein Teamgenerator')
        print('close')
        file.close()
        print('closed')
        
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
            print(len(indexes), ", teamA")
            return [indexes, 'teamA']
        else:
            indexes = selModelB.selectedIndexes()
            if (indexes != [] ):
                indexes = selModelB.selectedIndexes()
                print(len(indexes), ", teamB")
                return [indexes, 'teamB']
                       
        return [[], '']
    
    
    def addPlayer(self):
        '''Dependent on the focus one row on Table A or Table B is added'''
        
        currentTable = self.getSelectedPlayers()[1]
        if currentTable == 'teamA':
            print("\n§§§ addPlayer in teamA §§§")
            print(" len(tgmA.get_ptable())=",len(tgmA.get_ptable()))
            print(" len(tg.teamA.players)=",len(tg.teamA.players))        
            print(" len(tgmB.get_ptable())=",len(tgmB.get_ptable()))
            print(" len(tg.teamB.players)=",len(tg.teamB.players))
            tgmA.insertRows(0,1)
            print(" len(tgmA.get_ptable())=",len(tgmA.get_ptable()))
            print(" len(tg.teamA.players)=",len(tg.teamA.players))        
            print(" len(tgmB.get_ptable())=",len(tgmB.get_ptable()))
            print(" len(tg.teamB.players)=",len(tg.teamB.players))            
        elif currentTable == 'teamB':
            print("\n§§§ addPlayer in teamB §§§")
            print(" len(tgmA.get_ptable())=",len(tgmA.get_ptable()))
            print(" len(tg.teamA.players)=",len(tg.teamA.players))        
            print(" len(tgmB.get_ptable())=",len(tgmB.get_ptable()))
            print(" len(tg.teamB.players)=",len(tg.teamB.players))
            tgmB.insertRows(0,1)
            print(" len(tgmA.get_ptable())=",len(tgmA.get_ptable()))
            print(" len(tg.teamA.players)=",len(tg.teamA.players))        
            print(" len(tgmB.get_ptable())=",len(tgmB.get_ptable()))
            print(" len(tg.teamB.players)=",len(tg.teamB.players))
        else:
            showMessage('TeamA oder TeamB selektieren!')             
        self.refreshGUI()


    def callBerechneManschaften(self):
        ''' Calculate best Teams
        '''
        
        tg.teamA.shiftPlayersFromTeam(tg.teamB)
        
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
            showMessage('Erst Spieler selektieren!')
        
        self.refreshGUI()   
    
    def removeFromTable(self):
        indexes = self.getSelectedPlayers()
        selectetPlayers = []
        
        for index in indexes[0]:
            selectetPlayers.append(int(index.row()))
            
        #: set() liste of unique elements
        selectetPlayers = list(set(selectetPlayers))
        selectetPlayers.sort(reverse = True)
        print("selectetPlayers",selectetPlayers)    
        if indexes[1] == 'teamA':
            for i in selectetPlayers:
                tg.teamA.removeByIndex(i)
            
        elif indexes[1] == 'teamB':
            for i in selectetPlayers:
                tg.teamB.removeByIndex(i)
        else:
            showMessage('Erst Spieler selektieren!')
        
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
        
    def updateTextBoxes(self):
        #: TextBoxes A
        calculatedTeamWindow.gesammt_A.setText("%.2f" % tg.teamA.calcTeampoints())
        calculatedTeamWindow.angriff_A.setText(str(tg.teamA.attackpoints))
        calculatedTeamWindow.abwehr_A.setText(str(tg.teamA.defencepoints))
        calculatedTeamWindow.tor_A.setText(str(tg.teamA.keeperpoints))
        #: TextBoxes B
        calculatedTeamWindow.gesammt_B.setText("%.2f" % tg.teamB.calcTeampoints())
        calculatedTeamWindow.angriff_B.setText(str(tg.teamB.attackpoints))
        calculatedTeamWindow.abwehr_B.setText(str(tg.teamB.defencepoints))
        calculatedTeamWindow.tor_B.setText(str(tg.teamB.keeperpoints))
    
    def refreshGUI(self):
        ''' method to refresh all displayed data '''
#        global tgmA 
#        tgmA = TeamGeneratorModel(tg.teamA.players)
        tgmA.ptableUpdate(tg.teamA.players)
        calculatedTeamWindow.tableView_A.setModel(tgmA)
        proxyA = PlayerFilterProxyModel(tgmA)
        proxyA.setSourceModel(tgmA)
        calculatedTeamWindow.tableView_A.setModel(proxyA)  
        
#        global tgmB 
#        tgmB = TeamGeneratorModel(tg.teamB.players)
        tgmB.ptableUpdate(tg.teamB.players)        
        calculatedTeamWindow.tableView_B.setModel(tgmB)
        proxyB = PlayerFilterProxyModel(tgmB)
        proxyB.setSourceModel(tgmB) 
        calculatedTeamWindow.tableView_B.setModel(proxyB)
 
        self.updateTextBoxes()
        
#===================================================================================================   
class playerSelectWind:
    
    def __init__(self):
        playerSelectWindow.add_Btn.clicked.connect(lambda: self.playerSelectWindowAdd())
        playerSelectWindow.remove_Btn.clicked.connect(lambda: self.removeFromTable())
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
        print("gotoNextWindow1")
        
        playerProTeam = len(tg.teamA.players)
        if (playerProTeam > 1):        
            print("playerProTeam =", playerProTeam)
            if playerProTeam % 2 != 0:          
                playerProTeam = playerProTeam + 1
                
            message = str('Es gibt ' +
                        str(int( tg.binomial(playerProTeam, int(playerProTeam*0.5)))) +
                        ' verschiedene Kombinationen. Es kann also dauern ...')
            waitingCalculation.textBrowser.setText(message)
            waitingCalculation.show()
        else:
            showMessage('Bitte erst ein paar Spieler wählen!')
    
    
                    
    def getSelectedPlayers(self):
        ''' Get the list currently selected indexes + table name
        
        :returns: [ [List of selected players], 'TableName' ]
        :rtype: [ [], str]
        '''
        print("getSelectedPlayers")    
        
        selModelF = playerSelectWindow.tableView_full.selectionModel()
        selModelA = playerSelectWindow.tableView_A.selectionModel()
        
        
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
            showMessage('Erst Spieler selektieren!')
        
        self.refreshGUI()  

     
    def playerSelectWindowAdd(self):
        print("\n$$$$ playerSelectWindowAdd $$$$")
        print(" len(tgmF.get_ptable())=",len(tgmF.get_ptable()))
        print(" len(tg.fullTeam.players)=",len(tg.fullTeam.players))
        print(" len(tgmA.get_ptable())=",len(tgmA.get_ptable()))
        print(" len(tg.teamA.players)=",len(tg.teamA.players))
        tgmF.insertRows(0,1)
        print(" len(tgmF.get_ptable())=",len(tgmF.get_ptable()))
        print(" len(tg.fullTeam.players)=",len(tg.fullTeam.players))
        print(" len(tgmA.get_ptable())=",len(tgmA.get_ptable()))
        print(" len(tg.teamA.players)=",len(tg.teamA.players))
        print("$$$$ playerSelectWindowAdd $$$$")
        self.refreshGUI()
        print("$$$$ playerSelectWindowAdd After GUI refresh $$$$")
        print(" len(tgmF.get_ptable())=",len(tgmF.get_ptable()))
        print(" len(tg.fullTeam.players)=",len(tg.fullTeam.players))
        print(" len(tgmA.get_ptable())=",len(tgmA.get_ptable()))
        print(" len(tg.teamA.players)=",len(tg.teamA.players))
    
    def removeFromTable(self):
        indexes = self.getSelectedPlayers()
        selectetPlayers = []
        
        for index in indexes[0]:
            selectetPlayers.append(int(index.row()))
            
        #: set() liste of unique elements
        selectetPlayers = list(set(selectetPlayers))
        selectetPlayers.sort(reverse = True)
        print("selectetPlayers",selectetPlayers)    
        if indexes[1] == 'fullTeam':
            for i in selectetPlayers:
                tg.fullTeam.removeByIndex(i)
            
        elif indexes[1] == 'teamA':
            for i in selectetPlayers:
                tg.teamA.removeByIndex(i)
        else:
            showMessage('Erst Spieler selektieren!')
        
        self.refreshGUI()
      
    def refreshGUI(self):
        #: tableView_full is connected with fullTeam
#        global tgmF
#        tgmF = TeamGeneratorModel(tg.fullTeam.players)
        tgmF.ptableUpdate(tg.fullTeam.players)
        playerSelectWindow.tableView_full.setModel(tgmF)
        proxyF = PlayerFilterProxyModel(tgmF)
        proxyF.setSourceModel(tgmF)
        playerSelectWindow.tableView_full.setModel(proxyF)
        
        #: tableView_A is connected with teamA
#        global tgmA        
#        tgmA = TeamGeneratorModel(tg.teamA.players)
        tgmA.ptableUpdate(tg.teamA.players)
        playerSelectWindow.tableView_A.setModel(tgmA)
        proxyA = PlayerFilterProxyModel(tgmA)
        proxyA.setSourceModel(tgmA)
        playerSelectWindow.tableView_A.setModel(proxyA)


#===================================================================================================
class waitingCalculationWind:
    def __init__(self):
        waitingCalculation.calculateButton.clicked.connect(lambda: self.calculate())
        waitingCalculation.cancelButton.clicked.connect(lambda: self.cancel())
    
    def calculate(self):
        print("### callBerechneManschaften() ###")
        tg.berechneMannschaften()    
        print("########### TEAM A: ############")
        tg.teamA.print()
        print("########### TEAM B: ############")
        tg.teamB.print()
        playerSelectWindow.close()
        ctwin.refreshGUI()
        calculatedTeamWindow.show()
        waitingCalculation.close()        
   
    def cancel(self):
        waitingCalculation.close()        
        

#===================================================================================================
def showMessage(message = ""):
    ''' Pop-up of a simple message box
    
    :params message: Text to display
    :message type: str
    :returns: -
    '''
    qwid = QtGui.QWidget()
    qmb  = QtGui.QMessageBox(qwid)
    qmb.setText(message)
    qmb.setWindowTitle('Team Generator Message')
    qmb.setDefaultButton(QtGui.QMessageBox.Ok) 
    qmb.show()
    ret = qmb.exec_()
    print(ret)
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
    tgmF = TeamGeneratorModel(tg.fullTeam.players) # All players empty !

    tgmA = TeamGeneratorModel(tg.teamA.players)#[[tg.fullTeam.players.name], [tg.fullTeam.players.attackpoints], [tg.fullTeam.players.defencepoints]] ) #     ['1', '2', '3'])
    tgmB = TeamGeneratorModel(tg.teamB.players)
    
    
    #: Needed to start Qt
    app = QtGui.QApplication(sys.argv)
    
    #: Now loading the Qt Designer ".ui"-files and instanciating the user interfaces:
    welcomeWindow =         uic.loadUi('./.GUI/welcomeWindow.ui')
    playerSelectWindow =    uic.loadUi('./.GUI/playerSelectWindow.ui')     
    calculatedTeamWindow =  uic.loadUi('./.GUI/calculatedTeamWindow.ui')   
    waitingCalculation =    uic.loadUi('./.GUI/waitingCalculation.ui')
    
    #: To setup all the Qt models and Views of for each window one class is instanciated
    wcwin = welcomeWind()
    ctwin = calculateTeamWind(tgmA, tgmB)
    pswin = playerSelectWind()
    waitwin = waitingCalculationWind() 
    
    #:Showing the first window. All the next windows are
    #:called from the windows before. 
    welcomeWindow.show()
    print('GUI up and running now ')
     
    app.exec_()
    print('----- END of TeamGenerator_GUI -----')