import numpy as np
from sklearn import metrics

traindatafile = open('TrD1.csv','r')

matrix = []
for i in range(3):
    matrix.append([0,0])

for line in traindatafile:
    spline = line.split(',')
    out = int(spline[-1])
    if spline[31] == 'Yes':
        matrix[out][0] += 1
    elif spline[31] == 'No':
        matrix[out][1] += 1
    else:
        print 'PAAANIC'
print matrix
