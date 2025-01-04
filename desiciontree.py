#Q] Write a program to implement Data Tree Algorithm using given data set
# Import necessary libraries
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
import numpy as np
import matplotlib.pyplot as plt 
# Example dataset
# Features: [Hours Studied, Attendance]
X = np.array([[3, 7], [2, 5], [1, 8], [4, 6], [5, 9]])
# Labels: Pass(1) or Fail(0)
y = np.array([1, 0, 0, 1, 1])
# Create and train the Decision Tree Classifier
clf = DecisionTreeClassifier(criterion='gini', max_depth=3, random_state=42)
clf.fit(X, y)
# Predict outcomes for new data
new_data = np.array([[3, 6], [1, 9]])
predictions = clf.predict(new_data)
# Display the decision tree
print("Predicted outcomes for new data:", predictions)
print("\nDecision Tree Structure:\n")
tree.plot_tree(clf)
plt.show()