import numpy as np
import matplotlib.pyplot as plt
import warnings
from collections import Counter
import pdb

dataset = {'k': [[1,2],[2,3],[3,1]], 'r':[[6,5],[7,7],[8,6]]}
new_features = [5,7]

plt.subplot(2,1,1)
for i in dataset:
    for ii in dataset[i]:
        plt.scatter(ii[0],ii[1], s= 100, color=i)

# This could be used to replace 'for statement' above
#[[plt.scatter(ii[0],ii[1],s=100, color=i) for ii in dataset[i]] for i in dataset]        


plt.scatter(new_features[0],new_features[1], s = 100)

def k_nearest_neighbour(data, predict, k = 3):
    if len(data) >= k:
        warnings.warn('K is set to a value less than total groups')
    distance = []
    # SIMILAR TO FIRST FOR LOOP
    for group in data:
        for features in data[group]:
            #euclidean_distance = sqrt((features[0]-predict[0])**2 + (features[0]-predict[0])**2 )
            euclidean_distance = np.linalg.norm(np.array(features)-np.array(predict))
            distance.append([euclidean_distance, group])

    ## THIS TELLS THE MOST VOTES A GROUP GOT SINCE k=3 3 VOTES ARE CONSIDERED
    votes = [i[1] for i in sorted(distance)[:k ]]
    
    ## TO CHECK WHICH GROUP HAS MOST COMMON VOTES
    vote_result = Counter(votes).most_common(1)[0][0]
    print(vote_result)
    return vote_result

## FUNCTION CALL
result = k_nearest_neighbour(dataset,new_features,k=3)


## GROUPING THE RESULT TO CLOSEST NEIGHBOUR
plt.subplot(2,1,2)
for i in dataset:
    for ii in dataset[i]:
        plt.scatter(ii[0],ii[1], s= 100, color=i)

plt.scatter(new_features[0],new_features[1], s = 100, color=result)
plt.show()
