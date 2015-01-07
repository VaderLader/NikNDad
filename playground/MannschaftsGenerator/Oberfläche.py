# -*- coding: utf-8 -*-

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.uic import *

app = QApplication(sys.argv)
s1 = loadUi('Oberfläche.ui')
s2 = loadUi('Oberfläche2.ui')


s1.show()

s1.startWeiterBtn.clicked()
s2.show()
sys.exit(app.exec_())