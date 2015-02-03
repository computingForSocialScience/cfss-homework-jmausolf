import csv
import sys
import pandas
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd




data_zip = pandas.read_csv("permits_hydepark.csv", header=None, usecols=[28,35,42, 49, 56, 63, 70, 77, 84])

#print data_zip

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
#For whichever reason, would only work one at a time. 
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


def df_clean():
	df_clean = []
	for i in range(0, len(df_list)):
		new = str(df_list[i])
		clean = new[0:5]
		df_clean.append(clean)
	return df_clean

zip_codes = df_clean()


print zip_codes

"""def zip_code_barchart():
	plt.figure();
	zip_codes.plot(kind='bar'); 
	plt.show()"""


#zip_code_barchart()

import matplotlib.pyplot as plt
from pylab import *


n = zip_codes
figure()
hist(n)
show()


import matplotlib.pyplot as plt

n = zip_codes
fig, axes = plt.subplots(1, 2, figsize=(12, 4))
axes[0].hist(n)
axes[0].set_title("Zip Codes")
axes[0].set_xlim((min(n), max(n)))




