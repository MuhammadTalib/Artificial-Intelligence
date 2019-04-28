import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import os


df=pd.read_csv('olxcardata.csv', delimiter=',', encoding = "ISO-8859-1")
df.head()

print(df.columns)