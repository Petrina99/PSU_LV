import os
import sys

fo = open(os.path.join(sys.path[0], "SMSSpamCollection.txt"), "r")

spam = []
ham = []

brojac_spam = 0
brojac_ham = 0

for line in fo:
    if line.startswith("ham"):
        brojac_ham += 1
    else:
        brojac_spam += 1
    
    