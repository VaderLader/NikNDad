from PyQt4 import QtCore, uic, QtGui
import sys

if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    app.setStyle("cleanlooks")
    
    #DATA
    data = ["one", "two", "three", "four", "five"]

    listView = QtGui.QListView()    
    listView.show()

    model = QtGui.QStringListModel(data)
    
    listView.setModel(model)
    
    
    combobox = QtGui.QComboBox()
    combobox.setModel(model)
    combobox.show()
    
    listView2 = QtGui.QListView()
    listView2.show()
    listView2.setModel(model)
    

    sys.exit(app.exec_())
