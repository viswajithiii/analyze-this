yesno =[14,33] #mvar_14 and mvar_33
inputfile = open('TrD1_test.csv','r')
outputfile = open('TrD1_test.arff','w')
outputfile.write('@RELATION Crime1Train_testData\n\n')

for i in range(1,41):
    if i in yesno:
        vartype = '{0,1}'
    else:
        vartype = 'NUMERIC'
    outputfile.write('@ATTRIBUTE mvar_' + unicode(i) + ' ' + vartype + '\n')

outputfile.write('@ATTRIBUTE output {0,1,2}\n')

outputfile.write('\n@DATA\n')
for line in inputfile:
    spline = line.split(',')
    spline[-1] = spline[-1][0] + '\n'
    for i in range(len(spline)):
        if len(spline[i]) == 0:
            spline[i] = '?'
    for varindex in yesno:
        if spline[varindex-1] == 'Yes':
            spline[varindex-1] = '1'
        elif spline[varindex-1] == 'No':
            spline[varindex-1] = '0'
    outputfile.write(','.join(spline))
    if len(spline[-1]) == 0:
        outputfile.write('\n')
