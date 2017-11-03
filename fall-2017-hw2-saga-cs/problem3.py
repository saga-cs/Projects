def full_paths(path_components, base_path='/'):
	fp =[]
	np=[]
	initial = [base_path]
	for path in path_components:
		if isinstance(path,str):
			path = [path]
		fp.append(path)
	for path in fp:
		if len(path)==1:
			initial=[x+path[0]+'/' for x in initial]
		else:
			for x in initial:
				for i in range(len(path)):
					np.append(x)
			initial=np
			np=[]
			for i in range((int)(len(initial)/len(path))):
				for x in path:
					np.append(x)
			path=np
			np=[]		
			initial = [x+ y+'/' for x,y in zip(initial,path)]
	for i in initial:
		i=i[:-1]
		np.append(i)
	print(np)