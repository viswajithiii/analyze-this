import numpy as np

traindatafile = open('Training_Dataset.csv','r')
c1file = open('TrD1.csv','w')
c2file = open('TrD2.csv','w')

firstlineseen = False
for line in traindatafile:
    if not firstlineseen:
        firstlineseen = True
        continue
    splitline =line.split(',')
    crime = int(splitline[1][-1])
    if crime == 1:
        crimeone += 1
        c1file.write(','.join(splitline[2:]))
    else:
        crimetwo += 1
        c2file.write(','.join(splitline[2:]))
