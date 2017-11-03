x = input('Enter list 1:')
y = input('Enter list 2:')
x = x.replace(" ", "")
y = y.replace(" ", "")
y= set(y.split(','))
x= set(x.split(','))
z=x&y
print(list(map(int,z)))