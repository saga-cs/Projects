#!/usr/bin/env python3

from urllib.request import urlretrieve

print('Downloading 189 MB file, please be patient...')
urlretrieve('https://data.cityofchicago.org/api/views/4ijn-s7e5/rows.csv?accessType=DOWNLOAD',
            filename='Food_Inspections.csv')
