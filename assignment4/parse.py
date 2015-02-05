### Designed to Run in MacOSX Terminal. "Open" commands do not run in Linnux.

# Import Packages
import csv
import sys
import pandas
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter
import subprocess
import time


# Read CSV File
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





# *************** Latitude and Longitude Function ******************* #


# Data for Functions from CSV
data = readCSV('permits_hydepark.csv')

# INITIAL FUNCTIONS
# Lat-Long
def latlongfunt():
	data = readCSV('permits_hydepark.csv')
	latlong = []
	for i in range(0, len(data)):
		z = str(data[i])
		new = z[-40:-3]
		latlong.append(new)
	return latlong

# Latitude
def latitude():
	lat = []
	for i in range(0, len(data)):
		data_string = str(data[i])
		lat_str_data = data_string[-40:-23]
		lat_data = float(lat_str_data)
		lat.append(lat_data)
	return lat

# Longitude
def longitude():
	longe= []
	for i in range(0, len(data)):
		data_string = str(data[i])
		longe_str_data = data_string[-21:-3]
		long_data = float(longe_str_data)
		longe.append(long_data)
	return longe



# Average Latitude-Longitude
def get_avg_latlng():
   """Shows the averge latitude and longitude of
   construction permits in Hyde Park."""

   data = readCSV('permits_hydepark.csv')

   lat = latitude()
   longe = longitude()
   for var in data:
      avg_lat = sum(lat)/(len(lat))
      avg_longe = sum(longe)/(len(longe))
   print "*"*40
   print "Average LATITUDE and LONGITUDE: "
   print (avg_lat, avg_longe)
   print "*"*40







# ***************** Zip Code Function ******************* #


# Panda's Data Frame from CSV
df = pandas.read_csv("permits_hydepark.csv", header=None)

#Individual Data Columns
df28 = df[28]
df35 = df[35]
df42 = df[42]
df49 = df[49]
df56 = df[56]
df63 = df[63]
df70 = df[70]
df77 = df[77]
df84 = df[84]

#Appending the Data Columns as a Panda Series
#For whatever reason, this would only work one at a time. 
df_28_35 = df28.append(df35)
df_28_42 = df_28_35.append(df42)
df_28_49 = df_28_42.append(df49)
df_28_56 = df_28_49.append(df56)
df_28_63 = df_28_56.append(df63)
df_28_70 = df_28_63.append(df70)
df_28_77 = df_28_70.append(df77)
df_28_84 = df_28_77.append(df84)

#Rename combined series
df_combined = df_28_84

#Removing NaN values
df_new = pandas.Series.dropna(df_combined)

#Convert Panda Series to Python List
df_list = df_new.tolist()

# Clean up Zip Codes and Export as a Integer List
def df_clean():
	"""Takes the combined Pandas series of zip codes,
	cleans them, and makes an integer list."""
	df_clean = []
	for i in range(0, len(df_list)):
		new = str(df_list[i])
		clean = new[0:5]
		clean_int = int(clean)
		df_clean.append(clean_int)
	return df_clean


# Define Zip Code Lists Calling the df_clean function
zip_codes = df_clean()


# Make and Save JPG of Zip Code Bar Chart
def zip_code_barchart():
	"""Counts the cleaned list of zip codes and makes a 
	custom bar chart, saving the result as a JPG."""

	# Create counts of zip codes. 
	zipcode_counts = Counter(zip_codes)

	#matplotlib.interactive(True)
	plt.bar(range(len(zipcode_counts)), zipcode_counts.values(), align='center', color='g')
	plt.xticks(range(len(zipcode_counts)), zipcode_counts.keys())
	plt.xticks(rotation=70)
	plt.yticks(range(0, 6))
	plt.title('Contractor Zipcode Bar Chart')
	plt.xlabel('Contractor Zipcodes')
	plt.ylabel('Frequency')
	plt.grid(True)
	plt.draw()
	plt.savefig('bar.jpg')
	subprocess.call("open bar.jpg", shell=True)






# Calling several combinations of funtions from shell

sys_arg = sys.argv  


try: 
	first_arg = sys_arg[1]
	if first_arg == "latlong": get_avg_latlng()
	elif first_arg == "bar": zip_code_barchart()
		

	elif first_arg == "latlong, bar": 
		get_avg_latlng()
		time.sleep(1.5)
		zip_code_barchart()


	elif first_arg == "bar, latlong": 
		zip_code_barchart()
		time.sleep(1.5)
		get_avg_latlng()


	else: print("This argument is not recognized.")


except:
	print("Argument Error: Please specify at least one argument  such as 'latlong' or 'bar' or 'latlong, bar'")  
