import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
from sklearn import preprocessing, model_selection
import pandas as pd
import pdb

df = pd.read_csv('titanic.csv')
#breakpoint()
df.drop(['body','name'],1,inplace = True)
#df.convert_objects(convert_numeric=True)
df.fillna(0, inplace = True)
print(df.head())




def handle_non_numerical_data(df):
    columns = df.columns.values
    #print(columns)

    for column in columns:
        test_digit_values = {}
        def convert_to_int(val):
            return text_digit_vals[val]

handle_non_numerical_data(df)
