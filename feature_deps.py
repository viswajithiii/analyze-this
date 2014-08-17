import numpy as np
from sklearn import metrics

traindatafile = open('TrD1.csv','r')


big_out = []
big_a = []
floatfeatures = [0,2,7,10,15,16,17,18,22,24,27,28,30,32,35,36,37]
yesno = [12,31]
big_missingvalues = [0]*39
for i in range(39):
    big_out.append([])
    big_a.append([])

for line in traindatafile:
    for i in range(39):
        spline = line.split(',')
        if i in floatfeatures:
            try:
                f = float(spline[i])
                big_a[i].append(f)
                big_out[i].append(int(spline[-1]))
            except ValueError:
                big_missingvalues[i] += 1
        elif i in yesno:
            if spline[i] == 'Yes':
                big_a[i].append(1)
                big_out[i].append(int(spline[-1]))
            elif spline[i] == 'No':
                big_a[i].append(0)
                big_out[i].append(int(spline[-1]))
            else:
                big_missingvalues[i] += 1
        else:
            try:
                f = int(spline[i])
                big_a[i].append(f)
                big_out[i].append(int(spline[-1]))
            except ValueError:
                big_missingvalues[i] += 1



for i in range(len(big_out)):
    if i <= 8:
        trueval = i+1
    else:
        trueval = i+2
    print 'mvar_'+ unicode(trueval) + ',' + unicode(np.mean(big_a[i])) + ',' + unicode(np.std(big_a[i])) + ',' + unicode(big_missingvalues[i]) + ',' + unicode(metrics.normalized_mutual_info_score(big_a[i],big_out[i]))
