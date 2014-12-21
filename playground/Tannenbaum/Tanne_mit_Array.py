#!/usr/bin/env python3
# funny comment :)
import sys

TestFeld = [["1","2","3","4"],["5","6","7","8"],["9","A","B","C"]]
print ("TesFeld Länge: ", len(TestFeld), " !")
print (TestFeld)

for x in TestFeld:
    print

# Feld [x][y]
Feld = [
    [" "," "," "," "," "," "," "],
    [" "," "," "," "," "," "," "],
    [" "," "," "," "," "," "," "],
    [" "," "," "," "," "," "," "],
    [" "," "," "," "," "," "," "]
    ]
print ( len(Feld))
print ( len(Feld[0]))

# die Felder sind immer eins kürzer als len() angibt, da die Zählung mit 0 begint
xlaenge = len (Feld) - 1
ylaenge = len (Feld[0]) -1

#Live Edit by SohnyBohny

# Berechnung
hoehe = 1 
zielhoehe = 2
#x = 2
#while hoehe < zielhoehe:
        
def Berechnung():
    x = 2
    y1 = 2
    y2 = 2
    c = 1
    while x >= 0 :
        while y1 <= y2:
            Feld[x][y1] = "0"
            y1 += 1
        x -= 1
        c += c
        y1 -= c
        y2 += 1


def Ausgabe():
    x = xlaenge -1
    y = 0
    while x >= 0:
        y = 0
        while y < ylaenge:
            #sys.stdout.write("Feld[" + str(x)+ "][" + str(y) + "]=" + str(  (Feld[x][y])  )+ " ")
            sys.stdout.write(str(Feld[x][y])+ "")
            y += 1
        sys.stdout.write("\n")
        x -= 1


# while hoehe < zielhoehe:
#    y = 1
#    while y < luft:    # sollange bis y = luft
#        sys.stdout.write(" ")
#        y = y + 1
#   luft = luft - 1
#    tanne = hoehe * 2 -1
#    z = 0
#    while z < tanne:
#        sys.stdout.write("0")
#        z = z + 1
#
#    sys.stdout.write("\n")
#    hoehe = hoehe + 1
Berechnung()
Ausgabe()
x = input('\nTaste drücken zum beenden')

