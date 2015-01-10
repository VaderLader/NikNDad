# -*- coding: utf-8 -*-

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.uic import *

def startWeiter():
    s1.close()
    s2.show()
    
textBox=[]
spinAngriff=[]
spinAbwehr=[]
spinTor=[]

geoY = 20



def add():
    print ('add')
#==============================================================================
#      quit = QtGui.QPushButton('Close', self)
#  quit.setGeometry(10, 10, 60, 35)
#==============================================================================
    

app = QApplication(sys.argv)
s1 = loadUi('Oberfläche.ui')
s2 = loadUi('Oberfläche2.ui')


s1.show()

s1.startWeiterBtn.clicked.connect(startWeiter)

s2.addBtn.clicked.connect(add)


sys.exit(app.exec_())