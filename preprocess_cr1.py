important_indices = [0, 1, 2, 4, 10, 12, 15, 16, 17, 18, 22, 23, 24, 25, 26, 27, 28, 30, 32, 34, 35, 36, 37, 38,39] #39 is output
yesno = [12,31]
inputfile = open('TrD1_test.csv','r')
outputfile = open('TrD1_test_p.csv','w')

for line in inputfile:
    spline = line.split(',')
    if spline[12] == 'Yes':
        spline[12] = '1'
    elif spline[12] == 'No':
        spline[12] = '0'
    outputfile.write(','.join([spline[i] for i in important_indices]))
