# KMeans Clustering (Flat Clustering)

import matplotlib.pyplot as plt
import numpy as np

## Data for classification
data = np.array([[1,2],
             [1.5,1.8],
             [5,8],
             [8,8],
             [1,0.6],
             [9,11]])


#plt.scatter(data[:,0], data[:,1], s=150)
#plt.show()

colors = ["g","r","c","b","k","o"]

class KMeans:

    def __init__(self, k=2, tol=0.001, max_iter=300):
        ## k is for number of clusters to be created
        ## tolerances is for movement of the android
        ## max_iter is for number of iterations to cluster into centroid groups
        self.k = k
        self.tol = tol
        self.max_iter = max_iter

        
    def fit(self,data):
        self.centroids = {}

        ## CHOSES THE NUMBER OF CENTROIDS 
        for i in range(self.k):
            self.centroids[i] = data[i]
            

        ## Classifying datasets with centroids
        for i in range(self.max_iter):
            self.classifications = {}

            for i in range(self.k):
                self.classifications[i] = []

            for featureset in data:
                distances = [np.linalg.norm(featureset-self.centroids[centroid])for centroid in self.centroids]
                classification = distances.index(min(distances))
                self.classifications[classification].append(featureset)

            
            prev_centroids = dict(self.centroids)


            for classification in self.classifications:
                self.centroids[classification] = np.average(self.classifications[classification],axis=0)
                
            optimized = True

            for c in self.centroids:
                original_centroid = prev_centroids[c]
                current_centroid = self.centroids[c]
                if np.sum((current_centroid-original_centroid)/original_centroid*100.0) > self.tol:
                    optimized = False

            if optimized:
                break

            

    def predict(self,data):
        distances = [np.linalg.norm(data-self.centroids[centroid])for centroid in self.centroids]
        classification = distances.index(min(distances))
        return classification
        
    
kmeans = KMeans()        
kmeans.fit(data)

[plt.scatter(kmeans.centroids[centroid][0],kmeans.centroids[centroid][1],s=150,marker = 'x') for centroid in kmeans.centroids]

for classification in kmeans.classifications:
    color = colors[classification]
    for featureset in kmeans.classifications[classification]:
        plt.scatter(featureset[0],featureset[1],marker = 'o', s = 150)

plt.show()
