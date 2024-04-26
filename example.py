# from sklearn.neighbors import NearestNeighbors
# import numpy as np

# X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
# nbrs  = NearestNeighbors(n_neighbors = 1, algorithm='ball_tree').fit(X)
# distances, indices = nbrs.kneighbors(np.array([[2,2]]));
# print(distances)
# print(indices)

from nearestneighbourfinder import NearestNeighborsFinder;

# Queries
#  1. Which algoritham should we use?  
#  2. Data set size matters? Disease only expecting 5k records yearly. If we are processing 100k records 
#     this is a good approch or not ?
#  3. What will be ideal radius ? or how can we find the ideal radius ?


data_set = [[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]]

finder = NearestNeighborsFinder(dataset = data_set)
indices, distances = finder.find_nearest_of([[0, 1]])

print(indices)
print(distances)