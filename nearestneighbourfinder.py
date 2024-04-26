from sklearn.neighbors import NearestNeighbors
import numpy as np;
# Thing we should improve here
#    algorutham can be overridable


class NearestNeighborsFinder:
    def __init__(self, dataset):
        self.dataset =  np.array(dataset)
        self.nbrs  = NearestNeighbors(radius = 0.5, algorithm = "ball_tree").fit(self.dataset)

    def find_nearest_of(self, cord):
        cord_array = np.array(cord)
        return self.nbrs.kneighbors(cord_array)