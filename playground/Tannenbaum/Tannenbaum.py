class TannenBaum:
    '''This is my TannenBaum class'''
    maxhight = 20
    hight = 0
    stamm = 5
    def __init__(self, name = "Baum", hight = 5, stamm = 5):
        self.hight = hight
        self.stamm = stamm
        self.name = name
        print ('\n---TannenBaum erzeugt ----\n name =' , name, '\nHöhe =', hight) 
        print ('---------')
        pass

    
    # der Baum wurde schon gepflanzt ...
    def wachsen(self):
        print ('-')
        self.hight += 1
        print ('Der Baum', self.name, "ist gewachsen und hat die aktuelle Höhe",  self.hight, 'm')



# Hauptprogramm
tree = TannenBaum('Otto',10,7)
Baum = TannenBaum()

tree.wachsen()

print("Der Baum", tree.name, "ist", tree.hight, "hoch und sein Stamm hat die Höhe", tree.stamm)
print('---- ENDE ----')

