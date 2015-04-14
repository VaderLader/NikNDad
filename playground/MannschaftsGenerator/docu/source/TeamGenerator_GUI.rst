TeamGenerator_GUI module
========================
Das Module **TeamGenerator_GUI** erzeugt das GUI (Graphical User Interface) für den **Mannschaftsgenerator**.
Es wird PyQt4 benutzt.

Das Programm hat verschiedene Windows:

1. Das sind die Windows::

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

#. Qt 


	Data[tg.teamA.players] ---> DataModel[tgmA] 
    DataModel[tgmA]  ---> ProxyModel[proxyA]
    ProxyModel[proxyA]--->ViewModel[tableView_A]

	Bild einfügen vom YouTube Tutorial oder Qt selber
	http://www.google.de/imgres?imgurl=http%3A%2F%2Fwww.yasinuludag.com%2Fmvd.png&imgrefurl=http%3A%2F%2Fwww.yasinuludag.com%2Fblog%2F%3Fp%3D98&h=257&w=239&tbnid=1YUfi4zIIfxmOM%3A&zoom=1&docid=_Tv9gCP091DVHM&ei=_CAsVb_ZJIyHPZzagKgO&tbm=isch&iact=rc&uact=3&dur=1&page=2&start=24&ndsp=32&ved=0CKgBEK0DMCs
	
	
	
.. automodule:: TeamGenerator_GUI
    :members:
    :undoc-members:
    :show-inheritance:

	py:function:: enumerate(sequence[, start=0])