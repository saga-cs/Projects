import itertools
x = (list(itertools.permutations([0,1,2,3,4,5,6,7,8,9], 6)))
for i in x: 
	num1=100000*int(i[0])+10000*int(i[1])+1000*int(i[2])+100*int(i[3])+10*int(i[4])+int(i[5])
	num2=100000*int(i[1])+10000*int(i[2])+1000*int(i[3])+100*int(i[4])+10*int(i[5])+int(i[0]) 
	if 3*num1==num2:
		print(num1,' + ', num1 , ' + ', num1, ' = ', num2)	