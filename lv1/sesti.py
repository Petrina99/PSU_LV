import os
import sys

fo = open(os.path.join(sys.path[0], "SMSSpamCollection.txt"), "r")

spam = []
ham = []

brojac_spam = 0
brojac_ham = 0

broj_rijeci_ham = 0
broj_rijeci_spam = 0
usklicnik = 0

for line in fo:
    if line.startswith("ham"):
        brojac_ham += 1

        r = line.split(" ")

        for a in r:
            broj_rijeci_ham += 1

    else:
        brojac_spam += 1

        r = line.split(" ")

        if a.endswith("!\n"):
            usklicnik += 1

        for a in r:
            broj_rijeci_spam += 1

print("Prosjecan broj rijeci u porukama tipa ham je", (broj_rijeci_ham / brojac_ham))
print("Prosjecan broj rijeci u porukama tipa spam je", (broj_rijeci_spam / brojac_spam))
print("Broj rijeci tipa spam koji zavrsava usklicnikom je", usklicnik)