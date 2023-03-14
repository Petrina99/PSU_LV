import os
import sys

f1 = input("Unesite ime 1. datoteke: ")
f2 = input("Unesite ime 2. datoteke: ")

def average_spam(f): 

    fo = open(os.path.join(sys.path[0], f), "r")
    brojac = 0
    total = 0

    for line in fo:
        if line.startswith("X-DSPAM-Confidence:"):
            brojac += 1

            #partition vraca tuple od 3 clana, 1. clan je ono prije upisanog stringa, 2. clan je trazeni substring i 3. clan je string nakon trazenog substringa zbog toga pisemo [2] da bi dohvatili zadnji element tupla
            novi_string = line.partition("X-DSPAM-Confidence: ")[2]

            # pisemo [:-2] da bi makli zadnja 2 charactera u stringu jer nisu brojevi vec \n
            total += float(novi_string[:-2])
    
    print("Ime datoteke:", f)
    print("Average X-DSPAM-Confidence:", (total/brojac))

average_spam(f1)
average_spam(f2)