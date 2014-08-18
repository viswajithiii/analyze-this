variables = [u'mvar_1', u'mvar_2', u'mvar_3', u'mvar_5', u'mvar_12', u'mvar_14', u'mvar_17', u'mvar_18', u'mvar_19', u'mvar_20', u'mvar_24', u'mvar_25', u'mvar_26', u'mvar_27', u'mvar_28', u'mvar_29', u'mvar_30', u'mvar_32', u'mvar_34', u'mvar_36', u'mvar_37', u'mvar_38', u'mvar_39', u'mvar_40','output']
vartypes = ['NUMERIC','NUMERIC','NUMERIC','NUMERIC', 'NUMERIC', '{0,1}', 'NUMERIC','NUMERIC','NUMERIC','NUMERIC','NUMERIC','NUMERIC','NUMERIC','NUMERIC','NUMERIC','NUMERIC','NUMERIC','NUMERIC','NUMERIC','NUMERIC','NUMERIC','NUMERIC','NUMERIC','NUMERIC','{0,1,2}']
print len(variables)
print len(vartypes)
inputfile = open('TrD1_test_p.csv','r')
outputfile = open('TrD1_test_p.arff','w')
outputfile.write('@RELATION Crime1TestData\n\n')
for i in range(len(variables)):
    outputfile.write('@ATTRIBUTE ' + variables[i] + ' ' + vartypes[i] + '\n')

outputfile.write('\n@DATA\n')
for line in inputfile:
    spline = line.split(',')
    for i in range(len(spline)):
        if len(spline[i]) == 0:
            spline[i] = '?'
    spline[-1] = spline[-1][0]
    outputfile.write(','.join(spline)+'\n')
