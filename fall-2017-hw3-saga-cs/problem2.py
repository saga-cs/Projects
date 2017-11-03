import csv
import math
from datetime import datetime
import webbrowser

class Library(object):

	def __init__(self, data):
		self.name = data['NAME ']
		self.hours = data['HOURS OF OPERATION']
		self.address = data['ADDRESS']
		self.city = data['CITY']
		self.state = data['STATE']
		self.zip = data['ZIP']
		self.phone = data['PHONE']
		self.url = data['WEBSITE']
		loc = data['LOCATION'].strip('()').split(',')
		self.location = Coordinate(float(loc[0]), float(loc[1]))

	def refinetime(self,rawtime):
		hrs=[]
		self.rawtime=rawtime
		self.rawtime = self.rawtime.strip(' ')
		if self.rawtime!= 'Closed':	
			tlist = self.rawtime.split('-')
			for i in tlist:
				if 'PM' in i:
					x = i.split('PM')
					hour = int(x[0])
					if hour!= 12:
						hrs.append(hour + 12)
					else:
						hrs.append(hour)
				else:
					x = i.split('AM')
					hour = int(x[0])
					hrs.append(hour)
		else:
			hrs.append(self.rawtime)
		return hrs 

	def hoo(self,hrs):
		day ={}
		self.hrs=hrs
		garbage = self.hrs.split(';')
		for days in garbage:
			time = days.split(':')
			if '-' in time[0] and 'M' in time[0]:
				day['Mon'] = self.refinetime(time[1])
				day['Tue'] = self.refinetime(time[1])
				day['Wed'] = self.refinetime(time[1])
				day['Thu'] = self.refinetime(time[1])
			
			elif '-' not in time[0] and 'M' in time[0]:
				day['Mon'] = self.refinetime(time[1])
				day['Wed'] = self.refinetime(time[1])

			elif 'TU' in time[0]:
				day['Tue'] = self.refinetime(time[1])
				day['Thu'] = self.refinetime(time[1])

			elif 'F' in time[0] and 'SA' not in time[0]:
				day['Fri'] = self.refinetime(time [1])

			elif 'F' in time[0] and 'SA' in time[0]:
				day['Fri'] = self.refinetime(time [1])
				day['Sat'] = self.refinetime(time [1])

			if 'SU' in time[0]:
				day['Sun'] = self.refinetime(time [1])
		return day

	def open_website(self):
		return webbrowser.open_new_tab(self.url)

	def is_open(self, time):
		dow = time.strftime('%a')
		lhoo = self.hoo(self.hours)
		if lhoo[dow][0] == 'Closed':
			return False
		elif lhoo[dow][1]>time.hour>=lhoo[dow][0]:
			return True
		else:
			return False

	def distance(self, coord):		
		dist = self.location.distance(coord)
		return dist

	def full_address(self):
		libadd = self.address+'\n'+self.city+', '+self.state+' '+self.zip
		return libadd

	def __repr__(self):
		return 'Library(%s)' %(self.name)

class Coordinate:
	def __init__(self, latitude, longitude):
		self.latitude = math.radians(latitude)
		self.longitude = math.radians(longitude)

	@classmethod
	def fromdegrees(cls, latitude, longitude):
		return cls(latitude,longitude)

	def distance(self, coord):
		la1 = coord.latitude
		lo1 = coord.longitude
		la2 = self.latitude
		lo2 = self.longitude
		x = math.sin((la2-la1)/2)**2
		y = math.cos(la1)*math.cos(la2)*(math.sin((lo2-lo1)/2)**2)
		d = 2*3961*math.asin(math.sqrt(x+y))
		return d

	def as_degrees(self):
		return (math.degrees(self.latitude), math.degrees(self.longitude))
	
	def show_map(self):
		lat = self.as_degrees()[0]
		lon = self.as_degrees()[1]
		site = 'http://maps.google.com/maps?q='+str(lat)+','+str(lon)
		webbrowser.open_new_tab(site)

	def __repr__(self):
		return 'Coordinate(%s, %s)' % self.as_degrees()

class City(object):

	def __init__(self, filename):
		self.libraries = []
		f = open(filename, 'r', newline='')
		reader = csv.DictReader(f)
		for row in reader:						
			self.libraries.append(Library(row))

	def nearest_library(self, coord):
		library = self.libraries[0]
		dis = library.distance(coord)
		for lib in self.libraries:
			if lib.distance(coord)<dis:
				library = lib
				dis = library.distance(coord)
		return library
				