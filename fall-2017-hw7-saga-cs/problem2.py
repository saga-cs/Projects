import pandas as pd
from datetime import datetime 
import numpy as np

def search_by_zip(dataframe):
	date = datetime(2016, 11, 1)
	""" Finds the restaurants that have failed an inspection since 11/1/2016 within ZIP code 60661
		Arguments:
		dataframe -- the csv file containing restaurant data
		Returns:
		dataframe of all the columns for restaurants matching the specified criterias."""
	
	rest = dataframe[(dataframe['Zip'] == 60661) &
                (dataframe['Facility Type'] == 'Restaurant')
                & (dataframe['Results'] == 'Fail')
                & (pd.to_datetime(dataframe['Inspection Date']) >= date)]
	
	return(rest)

def distance(la2,lo2):
	la1 = np.radians(41.8873906)
	lo1 = np.radians(-87.6459561)
	la = np.radians(la2)
	lo = np.radians(lo2)
	x = np.sin((la-la1)/2.0)**2
	y = np.cos(la1)*np.cos(la)*(np.sin((lo-lo1)/2.0)**2)
	d = 2*3961*np.arcsin(np.sqrt(x+y))
	return d

def search_by_location(dataframe):
	""" Finds the restaurants that have failed an inspection since 11/1/2016 within the distance of 0.5 Miles from Doctor Romano's House.
		Arguments:
		dataframe -- the csv file containing restaurant data
		Returns:
		dataframe of all the columns for restaurants matching the specified criterias."""
	date = datetime(2016, 11, 1)
	dataframe['Distance'] = dataframe.apply(lambda row: distance(row['Latitude'], row['Longitude']), axis=1)

	rest = dataframe[(dataframe['Facility Type'] == 'Restaurant')
            & (dataframe['Results'] == 'Fail')
            & (pd.to_datetime(dataframe['Inspection Date']) >= date)
            & (dataframe['Distance']<=0.5)]
	return rest.sort_values('Distance', ascending=True)

#def main():
#	file = pd.read_csv('Food_Inspections.csv')
#	print(search_by_location(file))
	#print(search_by_zip(file))


#if __name__ == '__main__':
#    main()