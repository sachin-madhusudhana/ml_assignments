import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets

## Loading the dataset

iris = datasets.load_iris()

X1_sepal = iris.data[:,[0,1]]
X2_petal = iris.data[:,[2,3]]
y = iris.target

print(X1_sepal[1:5,:])
print(X2_sepal[1:5,:])
print(y)
