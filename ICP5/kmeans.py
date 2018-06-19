# import matplotlib for plotting the clusters
import matplotlib.pyplot as plt
# import numpy library
import numpy as np
# from sklearn import kmeans
from sklearn.cluster import KMeans
# import random package to take random input dynamically
import random
# set the seed value to any int to get the same random values
random.seed(9)
# use uniform function to get the float values within range(4,7)
height=[round(random.uniform(4,7),2) for i in range(20)]
# use uniform function to get the float values within range(60,80)
weight=[round(random.uniform(60,80),2) for i in range(20)]
# numpy function vstack to stack the two arrays vertically
X = np.vstack((height,weight)).T
# print the 2d array
print(X)
# define the model and pass in number of clusters
kmeans = KMeans(n_clusters=3)
# fit the model to the array X
kmeans.fit(X)
# Scatter plot the datapoints with different colors assigned to various clusters
plt.scatter(X[:,0], X[:,1], c=kmeans.labels_, cmap='rainbow')
# Scatter plot the centroids with black color
plt.scatter(kmeans.cluster_centers_[:,0] ,kmeans.cluster_centers_[:,1], color='black')
# show the plot using matplotlib package
plt.show()
