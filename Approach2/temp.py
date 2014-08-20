from sklearn import metrics
from scipy import random

c = []
d = []
e = []

for i in range(10000):
    a = random.random_integers(0,1)
    b = random.standard_normal()
    c.append(a)
    d.append(b)
    e.append(a)
print metrics.normalized_mutual_info_score(c,d)
print metrics.adjusted_mutual_info_score(c,d)
print metrics.mutual_info_score(c,d)
print metrics.normalized_mutual_info_score(c,e)
print metrics.adjusted_mutual_info_score(c,e)
print metrics.mutual_info_score(c,e)
print c[:10]
print d[:10]
