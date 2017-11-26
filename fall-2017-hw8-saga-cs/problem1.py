import numpy as np
import matplotlib.pyplot as plt
import math
import multiprocessing 
import queue
import time
def mandelbrot(c, max_iterations=100):
	z = 0
	ctr = 0
	absz = math.sqrt(z.real**2 + z.imag**2)
	while(absz<=2 and ctr<=100):
		z = z**2 + c
		absz = math.sqrt(z.real**2 + z.imag**2)
		ctr+=1
	if absz>2:
		return ctr
	else:
		return 0 

def mandelbrot_serial(xmin, xmax, ymin, ymax, N=100):
	x = np.linspace(xmin,xmax,N)
	y = np.linspace(ymin,ymax,N)
	a = np.zeros(shape=(N,N))
	for i in range(N):
		for k in range(N):
			a[k,i] = mandelbrot(x[i] + y[k]*1j)
	return a 

def worker(xmin,xmax,ymin,ymax,results,div,N,cnt):
	x = np.linspace(xmin,xmax,div)
	y = np.linspace(ymin,ymax,N)
	a = np.zeros(shape=(N,div))
	for i in range(div):
		for k in range(N):
			a[k,i] = mandelbrot(x[i] + y[k]*1j)
	results.put((cnt,a))


def mandelbrot_static(xmin, xmax, ymin, ymax, N=100):
	processes = []
	num_processors = multiprocessing.cpu_count()
	results = multiprocessing.Queue()
	xmid = (abs(ymax-ymin)/num_processors)
	div = N//num_processors
	xmax = xmin  + xmid
	for i in range(num_processors):		
		p = multiprocessing.Process(target = worker, args = (xmin,xmax,ymin,ymax,results,div,N,i))
		p.start()
		processes.append(p)
		xmin = xmax
		xmax = xmin+xmid
	
	d = dict()
	for i in range(num_processors):
		m = results.get()
		d[m[0]] = m[1]

	arr = d[0]
	for i in range(1,num_processors):
		arr = np.concatenate((arr,d[i]),axis=1) 
		#print(b)
	for p in processes:
		p.join()

	return arr

def dynamic_worker(s):
	x = np.linspace(s[0],s[1],s[4])
	y = np.linspace(s[2],s[3],s[5])
	a = np.zeros(shape=(s[5],s[4]))
	for i in range(s[4]):
		for k in range(s[5]):
			a[k,i] = mandelbrot(x[i] + y[k]*1j)
	return (s[6],a)	

def mandelbrot_dynamic(xmin, xmax, ymin, ymax, N=100):
	num_processors = multiprocessing.cpu_count()
	pool = multiprocessing.Pool(num_processors)
	xmid = (abs(xmax-xmin)/num_processors)
	div = N//num_processors
	l =[]
	xmax = xmin  + xmid
	for i in range(num_processors):	
		l.append((xmin,xmax,ymin,ymax,div,N,i))
		xmin = xmax
		xmax = xmin+xmid		
	arr = pool.map(dynamic_worker, l)
	d=dict()
	for i in range(num_processors):
		d[arr[i][0]]= arr[i][1]
	a = d[0]
	for i in range(1,num_processors):
		a = np.concatenate((a,d[i]),axis=1) 
	return a

def main():
	start = time.time()
	mandelbrot_serial(-2.25,0.75,-1.5,1.5)
	end = time.time()
	print('Manderbolt serial runs in time : ',end - start)
	start = time.time()
	mandelbrot_static(-2.25,0.75,-1.5,1.5)
	end = time.time()
	print('Manderbolt static runs in time : ',end - start)
	start = time.time()
	arr = mandelbrot_dynamic(-2.25,0.75,-1.5,1.5)
	end = time.time()
	print('Manderbolt dynamic runs in time : ',end - start)	
	plt.imshow(arr , extent=[-2.25,0.75,-1.5,1.5])
	plt.show()	
	plt.savefig('Manderbolt.png')

if __name__ == '__main__':
	main()