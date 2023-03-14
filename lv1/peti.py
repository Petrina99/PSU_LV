import os
import sys

fo = open(os.path.join(sys.path[0], "song.txt"), "r")

rijeci = {}

for line in fo:
    r = line.split(" ")

    for a in r: 
        #micemo newline ak je nakraju stringa
        nova = a.rstrip('\n')

        #micemo zareze ak su nakraju stringa
        bez_zareza = nova.replace(",", "")
        
        #prebacujemo sve u lowercase jer su neke rijeci velikim slovom
        if bez_zareza.lower() in rijeci:
            rijeci[bez_zareza.lower()] += 1
        else:
            rijeci[bez_zareza.lower()] = 1

print(rijeci)

print("Rijeci koje se samo jednom pojavljuju: ")
for x in rijeci:
    if(rijeci.get(x) == 1):
        print(x, end=", ")