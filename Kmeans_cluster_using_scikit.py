import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans

X = np.array([[1,2],
             [1.5,1.8],
             [5,8],
             [8,8],
             [1,0.6],
             [9,11]])



clf = KMeans(n_clusters=3)
clf.fit(X)

centroids = clf.cluster_centers_
labels = clf.labels_

colors = ["g.","r.","c.","b.","k.","o."]

for i in range(len(X)):
    plt.plot(X[i][0],X[i][1], colors[labels[i]], markersize = 10)

plt.scatter(centroids[:,0], centroids[:,1], marker = 'x',s = 100)
plt.show()

