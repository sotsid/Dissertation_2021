# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 00:54:12 2021

@author: sotir
"""

import os
import glob
import pandas as pd
os.chdir("C:/Users/sotir/Downloads/qgis/crime data")
extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
#combine all files in the list
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
#export to csv
combined_csv.to_csv( "crimedata.csv", index=False, encoding='utf-8-sig')

crimedata = pd.read_csv("crimedata.csv")

type(crimedata)

crimev1 = crimedata.drop(['Crime ID', 'Reported by', 'Falls within', 'Location', 'Last outcome category', 'Context'], axis=1)
crimev2 = crimev1.dropna(subset = ['Longitude', 'Latitude', 'Crime type'])

# Get indexes where name column has value Other theft or Other crime and 

indexNames = crimev2[ (crimev2['Crime type'] == 'Other theft') & (crimev2['Crime type'] == 'Other crime') ].index

# Delete these row indexes from dataFrame
CrimeFinal = crimev2.drop(indexNames , inplace=True)





