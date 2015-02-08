# -*- coding: utf-8 -*-
"""
Created on Sun Feb  8 18:01:54 2015

@author: Niklas
"""

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.uic import *


fenster = loadUi('example_QTableView.ui')


fenster.tableView.setModell()







sys.exit(app.exec_())