from sklearn.decomposition import PCA
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
# Load the Iris dataset
data = load_iris()
X = data.data # Features
y = data.target # Labels
# Apply PCA to reduce the data to 2 dimensions
pca = PCA(n_components=2)
X_reduced = pca.fit_transform(X)
# Plot the reduced data
plt.scatter(X_reduced[:, 0], X_reduced[:, 1], c=y)
plt.title('PCA: Dimensionality Reduction')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.show()
# Print the explained variance (importance of each component)
print("Explained Variance Ratio:", pca.explained_variance_ratio_)