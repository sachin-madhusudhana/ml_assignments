
############# INCOMPLETE ################

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets, model_selection
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler

## Loading the dataset

iris = datasets.load_iris()

X1_sepal = iris.data[:,[0,1]]
X2_petal = iris.data[:,[2,3]]
y = iris.target

print(X1_sepal[1:5,:])
print(X2_petal[1:5,:])
print(y)


## Visualising the data

plt.subplot(2,1,1)
plt.scatter(X1_sepal[:,0] , X1_sepal[:,1], s=20, c=y)
plt.xlabel('sepal length')
plt.ylabel('sepal width')

plt.subplot(2,1,2)
plt.scatter(X2_petal[:,0] , X2_petal[:,1], s=20, c=y)
plt.xlabel('petal length')
plt.ylabel('petal width')

plt.show()


## Splitting and scaling for Training and testing of dataset

X_train_sepal, X_test_sepal, y_train_sepal, y_test_sepal = model_selection.train_test_split(X1_sepal,y,test_size=0.3)

print("Training samples for sepal", len(X_train_sepal))

print("Testing samples for sepal", len(X_test_sepal))


## Scaling

sc = StandardScaler()
X_train_sepal_std = sc.fit_transform(X_train_sepal)
X_test_sepal_std = sc.fit_transform(X_test_sepal)
X_combined_sepal_standard = np.vstack((X_train_sepal_std,X_test_sepal_std))
Y_combined_sepal = np.hstack((y_train_sepal, y_test_sepal))


## Linear  SVC


C_param_range = [0.01,0.1,1,10,100]
sepal_acc_table = pd.DataFrame(columns = ['C_parameter','Accuracy'])
sepal_acc_table['C_parameter'] = C_param_range
j = 0
for i in C_param_range:
    
    svm_linear = SVC(kernel = 'linear', C=i)
    svm_linear.fit(X_train_sepal_std,y_train_sepal)
    prediction = svm_linear.predict(X_test_sepal_std)
    print(prediction)
    sepal_acc_table.iloc[j,1] = accuracy_score(y_test_sepal,prediction)
    j+=1
    plt.subplot(3,2,j)
    plt.subplots_adjust(hspace = 0.4)
    plot_decision_regions(X = X_combined_sepal_standard
                      , y = Y_combined_sepal
                      , classifier = svm_linear
                      , test_idx = range(105,150))
print(sepal_acc_table)

 






