<<<<<<< HEAD
import functools
class FunctionalList(list):
	def __init__(self,lis):
		super().__init__(lis) 
	def map(self,func):
		newlist = FunctionalList(map(func,self))
		return newlist
	def filter(self,func):
		newlist = FunctionalList(filter(func,self))
		return newlist
	def reduce(self,func):
		value = functools.reduce(func,self)
		return value
=======
import functools
class FunctionalList(list):
	def __init__(self,lis):
		super().__init__(lis) 
	def map(self,func):
		newlist = FunctionalList(map(func,self))
		return newlist
	def filter(self,func):
		newlist = FunctionalList(filter(func,self))
		return newlist
	def reduce(self,func):
		value = functools.reduce(func,self)
		return value
>>>>>>> 1609239140c0b2fe80a6c596bfa09e55a09d46fd
