def returns(argtype):
	if not isinstance(argtype,type):
		raise TypeError(f'{argtype} is not a type object')
	def decorator(function):
		def inner(*args):
			if not isinstance(function(*args), argtype):
				raise TypeError('f should return a {}'.format( argtype.__name__))
			return function(*args)
		return inner
	return decorator