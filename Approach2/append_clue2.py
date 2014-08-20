dsname = 'Final_Dataset'

origfile = open(dsname+'.csv','r')
cluefile = open(dsname+'_Clue.csv','r')
outfile = open(dsname+'_clued.csv','w')

firstdone = False
mvar10 = []
for line in cluefile:
    if not firstdone:
        firstdone = True
        continue
    spline = line.split(',')
    mvar10.append(spline[-1][:-1])

counts = [0,0,0]
for v in mvar10:
    if v == '':
        counts[0] += 1
    elif v == '0':
        counts[1] += 1
    else:
        counts[2] += 1
print counts

firstdone = False
i = 0
for line in origfile:
    spline = line.split(',')
    if not firstdone:
        firstdone = True
        spline.insert(11,'mvar_10')
        outfile.write(','.join(spline))
        continue
    spline.insert(11,mvar10[i])
    outfile.write(','.join(spline))
    i += 1
