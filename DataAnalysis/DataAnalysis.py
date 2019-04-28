import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os


df=pd.read_csv('olxcardata.csv', delimiter=',', encoding = "ISO-8859-1")


#print(df.columns)
#print(df.describe())
#print(df.dtypes)
#print(df.describe(include = "all"))
#print(df.info)

missing_data = df.isnull()
#print(missing_data.head(500))

#for column in missing_data.columns.values.tolist():
    #print(column)
    #print (missing_data[column].value_counts())
   # print("")  

var = df.groupby('Fuel').Price.sum()
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ax1.set_xlabel('Fuel')
ax1.set_ylabel('Price')
ax1.set_title("Fuel Vs Price")
var.plot(kind='bar')
plt.show()

