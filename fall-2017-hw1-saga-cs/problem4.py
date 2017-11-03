import sys
N=sys.argv[1]
file=open('employees.csv','r')
Dict={}
for line in file:
	x=line.split(',')
	if x[5] == 'Salary':
		Dict.update({(x[0],x[1]):float((x[7].replace("$","")))})
for i in range(int(N)):
	value=Dict.values()
	Max=max(value)
	keyindex =  list(value).index(Max)
	key = list(Dict.keys())[keyindex]
	print(key[0].replace("\"",""),",",key[1].replace("\"",""),"   $",Max)
	del Dict[key] 
