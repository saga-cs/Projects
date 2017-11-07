from collections import namedtuple
import functools

def lru_cache(maxsize=128):
	def decorator(func):		
		currsize=0
		hits=0
		misses=0
		values = []	
		keys =[]

		def cache_info():
			cache_info = namedtuple('cache_info',['hits','misses','maxsize','currsize'])
			cache_info= cache_info(hits,misses,maxsize,currsize)	
			return cache_info

		@functools.wraps(func)
		def inner(*args):
			nonlocal currsize 
			nonlocal hits
			nonlocal misses
			nonlocal maxsize
			nonlocal values
			nonlocal keys
				
			if args not in keys:
				values.append(func(*args))
				keys.append(args)
				currsize+=1
				misses+=1
				if currsize>maxsize:
					keys.pop(0)
					values.pop(0)
					currsize-=1
			else:
				hits+=1

			i = keys.index(args)
			inner.cache_info = cache_info
			return values[i]

		return inner

	return decorator