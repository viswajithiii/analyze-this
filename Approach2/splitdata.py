from random import random

trainratio = 0.8
inputfile = open('TrD1.csv','r')
train = open('TrD1_train.csv','w')
test = open('TrD1_test.csv','w')

traincount = 0
for line in inputfile:
    if random() < trainratio:
        traincount += 1
        train.write(line)
    else:
        test.write(line)
print traincount
