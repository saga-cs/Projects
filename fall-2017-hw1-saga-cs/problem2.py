import sys
import math
import collections
fname = sys.argv[1]
file = open(fname,'r')
x=[]
index=0
for line in file:
	x.append(int(line))
	index+=1
file.close()
mean = sum(x)/index
print('Mean: ', mean)
s=0
for i in x:
	s+=(i-mean)**2
std = math.sqrt(s/(index-1))
print('Standard deviation: ', std)
mode = collections.Counter(x).most_common(1)
print('Mode: ',mode[0][0])
