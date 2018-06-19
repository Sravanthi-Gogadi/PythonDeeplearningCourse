import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
X = np.array([[5.1,60],
     [5.2,65],
     [5.3,68],
     [5.4,70],
     [5.5,75],
     [5.6,78],
     [5.7,80],
     [5.8,85],
     [5.9,90],
     [6.0,91],])
kmeans = KMeans(n_clusters=3)
kmeans.fit(X)
print(kmeans.labels_)
plt.scatter(X[:,0], X[:,1], c=kmeans.labels_, cmap='rainbow')
plt.scatter(kmeans.cluster_centers_[:,0] ,kmeans.cluster_centers_[:,1], color='black')
plt.show()
