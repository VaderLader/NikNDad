class TannenBaum:
    '''This is my TannenBaum class'''
    maxhight = 20
    hight = 0
    stamm = 5
    def __init__(self, init_name = "Baum", init_hight = 5, init_stamm = 5):
        self.hight = init_hight
        self.stamm = init_stamm
        self.name = init_name
        print ('\n--- TannenBaum erzeugt ---')
        print ('name =' , self.name, '\nHöhe =', self.hight, '\nstamm=', self.stamm) 
        print ('--------------------------\n')
        pass

    
    
    # der Baum wurde   schon gepflanzt ...
    def wachsen(self):
        print ('-')
        self.hight += 1
        print ('Der Baum', self.name, "ist gewachsen und hat die aktuelle Höhe",  self.hight, 'm')


#dskjhfakjsh
# Hauptprogramm
tree = TannenBaum('Otto',10,7)
Baum = TannenBaum()

tree.wachsen()

print("Der Baum", tree.name, "ist", tree.hight, "hoch und sein Stamm hat die Höhe", tree.stamm)
print('---- ENDE ----')

