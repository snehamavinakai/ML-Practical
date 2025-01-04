import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Sample data: X (independent variable) and y (dependent variable)
X = np.array([[1], [2], [3], [4], [5]])  # Feature (e.g., years of experience)
y = np.array([15000, 18000, 21000, 24000, 27000])  # Target (e.g., salary)

# Create a linear regression model
model = LinearRegression()

# Train the model on the data
model.fit(X, y)

# Make predictions
y_pred = model.predict(X)

# Display the model parameters
print(f"Coefficient (Slope): {model.coef_}")
print(f"Intercept: {model.intercept_}")

# Display the predicted values
print("\nPredicted Values:")
for i in range(len(X)):
    print(f"X = {X[i][0]}, Predicted y = {y_pred[i]}")

# Plot the data and the regression line
plt.scatter(X, y, color='blue', label='Data points')
plt.plot(X, y_pred, color='red', label='Regression line')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.title('Simple Linear Regression')
plt.legend()
plt.show()
