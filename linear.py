import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
#Sample Data
X=np.array([1,2,3,4,5]).reshape(-1,1)
y=np.array([1,3,2,5,4])
#Create and fit the model
linear_model = LinearRegression()
linear_model.fit(X,y)
#Predictions
y_pred=linear_model.predict(X)
#Plot
plt.scatter(X,y,color='blue')
plt.plot(X,y_pred,color='red')
plt.title("Linear Regression")
plt.xlabel('X')
plt.ylabel('y')
plt.show()
