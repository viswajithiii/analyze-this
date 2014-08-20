import numpy as np
from sklearn import metrics
from sklearn.feature_selection import chi2,f_classif

traindatafile = open('TrD2.csv','r')
totalpoints = 23779


big_out = []
big_a = []
floatfeatures = [0,2,7,10,15,16,17,18,22,24,27,28,30,32,35,36,37]
yesno = [12,31]
big_missingvalues = [0]*39
big_j = [0]*39
for i in range(39):
    big_out.append(np.zeros((totalpoints,),dtype = np.int))
    big_a.append(np.zeros(totalpoints))

for line in traindatafile:
    for i in range(39):
        spline = line.split(',')
        if i in floatfeatures:
            try:
                f = float(spline[i])
                big_a[i][big_j[i]] = f
                big_out[i][big_j[i]] = int(spline[-1])
                big_j[i] += 1
            except ValueError:
                big_missingvalues[i] += 1
        elif i in yesno:
            if spline[i] == 'Yes':
                big_a[i][big_j[i]] = 1
                big_out[i][big_j[i]] = int(spline[-1])
                big_j[i] += 1
            elif spline[i] == 'No':
                big_a[i][big_j[i]] = 0
                big_out[i][big_j[i]] = int(spline[-1])
                big_j[i] += 1
            else:
                big_missingvalues[i] += 1
        else:
            try:
                f = int(spline[i])
                big_a[i][big_j[i]] = f
                big_out[i][big_j[i]] = int(spline[-1])
                big_j[i] += 1
            except ValueError:
                big_missingvalues[i] += 1

important = []
impvarnumbers = []
for i in range(len(big_out)):
    if i <= 8:
        trueval = i+1
    else:
        trueval = i+2
    if i in floatfeatures:
        type = "Float"
    elif i in yesno:
        type = "Binary"
    else:
        type = "Int"

    big_a[i] = np.delete(big_a[i],np.s_[big_j[i]:])
    big_out[i] = np.delete(big_out[i],np.s_[big_j[i]:])
    assert big_missingvalues[i] + big_j[i] == totalpoints
    (a,b) = f_classif(big_a[i],big_out[i])
    print 'mvar_'+ unicode(trueval) + ',' + unicode(np.mean(big_a[i])) + ',' + unicode(np.std(big_a[i])) + ',' + unicode(big_missingvalues[i]) + ',' + unicode(metrics.normalized_mutual_info_score(big_a[i],big_out[i]))+ ',' + '%.15f' % (a[0]) + ',' + unicode(b[0]) + ',Type='+unicode(type)
    if b[0] < 0.01:
        important.append(i)
        impvarnumbers.append('mvar_'+unicode(trueval))


print 'Important indices = ' + unicode(important)
print 'Important vars = ' + unicode(impvarnumbers)
