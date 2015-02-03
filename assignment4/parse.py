import csv
import sys
import pandas
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def readCSV(filename):
    '''Reads the CSV file `filename` and returns a list
    with as many items as the CSV has rows. Each list item 
    is a tuple containing the columns in that row as stings.
    Note that if the CSV has a header, it will be the first
    item in the list.'''
    with open(filename,'r') as f:
        rdr = csv.reader(f)
        lines = list(rdr)
    return(lines)


### enter your code below


data = readCSV('permits_hydepark.csv')

data_zip = pandas.read_csv("permits_hydepark.csv", header=None, usecols=[28,35,42, 49, 56, 63, 70, 77, 84])


plt.figure();
data_zip.plot(kind='bar'); 
plt.show()

"""def zip_list():
	zip_list = []
	for i in data_zip:
		if i != "NaN":
			z = str(i)
			zip_list.append[z]
		return zip_list

print zip_list(), "zip_list" """


print "Panda columns: ***"
print data_zip
print len(data_zip)
print type(data_zip)

def latlongfunt():
	latlong = []
	for i in range(0, len(data)):
		z = str(data[i])
		new = z[-40:-3]
		latlong.append(new)
	return latlong

def latitude():
	lat = []
	for i in range(0, len(data)):
		data_string = str(data[i])
		lat_str_data = data_string[-40:-23]
		lat_data = float(lat_str_data)
		lat.append(lat_data)
	return lat


def longitiude():
	longe= []
	for i in range(0, len(data)):
		data_string = str(data[i])
		longe_str_data = data_string[-21:-3]
		long_data = float(longe_str_data)
		longe.append(long_data)
	return longe


#print data[1]


def get_avg_latlng():
   '''Shows the averge latitude and longitiude of
   construction permits in Hyde Park'''
   lat = latitude()
   longe = longitiude()
   for var in data:
      avg_lat = sum(lat)/(len(lat))
      avg_longe = sum(longe)/(len(longe))
   print "*"*40
   print "Average LONGITUDE and LATITUDE: "
   print (avg_lat, avg_longe)
   print "*"*40

get_avg_latlng()



"""def zip_code():
	zip_code1 = []
	for i in range(0, len(data)):
		data_string = str(data[i])
		zip_str_data = data_string[150: 250]
		data = data
		#zip_data = float(zip_str_data)
		zip_code1.append(zip_str_data)
	return zip_code1"""

#print zip_code()

#zip_code_barchart()

