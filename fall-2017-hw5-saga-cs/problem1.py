def only_python(func): 
	def inner(*args):
		for a in args:
			if a=='Python':
				return func(*args)
		return None
	return inner

