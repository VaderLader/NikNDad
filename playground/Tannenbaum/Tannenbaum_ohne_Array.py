# -*- coding: utf-8 -*-

import sys
print('Wie hoch soll der Baum werden?')
zielhoehe = int(sys.stdin.readline())
print('Wie hoch soll der Stamm werden?')
zielstammhoehe = int(sys.stdin.readline())
print('und wie breit (2 oder 3 oder 4)')
zielstammbreitzaeler = int(sys.stdin.readline())
luft = zielhoehe
tanne = 1
hoehe = 1


        # hoehe = 1 ... 10
while hoehe < zielhoehe:
    y = 1
    while y < luft:    # sollange bis y = luft
        sys.stdout.write(" ")
        y = y + 1
    luft = luft - 1
    tanne = hoehe * 2 -1
    z = 0
    while z < tanne:
        sys.stdout.write("0")
        z = z + 1

    sys.stdout.write("\n")
    hoehe = hoehe + 1

stammhoehe = 1
while stammhoehe < zielstammhoehe:
    stammzaeler = 1
    while stammzaeler < zielhoehe:
        sys.stdout.write(" ")
        stammzaeler = stammzaeler + 1
    stammbreitzaeler = 1
    while stammbreitzaeler < zielstammbreitzaeler:
        sys.stdout.write("0")
        stammbreitzaeler = stammbreitzaeler + 1
    sys.stdout.write("\n")
    stammhoehe = stammhoehe + 1
    
