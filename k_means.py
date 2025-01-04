import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Static data (X, Y coordinates of points)
X = np.array([
    [1, 2],
    [2, 3],
    [3, 3],
    [6, 5],
    [7, 7],
    [8, 6],
    [10, 10],
    [12, 9],
    [13, 11],
    [14, 12]
])

# Perform K-Means clustering (with 3 clusters)
kmeans = KMeans(n_clusters=3)
kmeans.fit(X)

# Get the cluster labels
labels = kmeans.labels_

# Plot the points, color-coded by cluster
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis')

# Plot the cluster centers (in red)
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='red', marker='X')

plt.title('K-Means Clustering')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
