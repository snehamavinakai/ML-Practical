import numpy as np

def get_user_input():
    print("Enter the number of data points:")
    n = int(input())
    print("Enter the number of features:")
    m = int(input())
    print("Enter the feature matrix (one row at a time, space-separated):")
    
    X = []
    for i in range(n):
        row = list(map(float, input().split()))
        if len(row) != m:
            raise ValueError(f"Expected {m} features per row, but got {len(row)}")
        X.append(row)
    
    print("Enter the target vector (space-separated):")
    y = list(map(float, input().split()))
    if len(y) != n:
        raise ValueError(f"Expected {n} target values, but got {len(y)}")
    
    return np.array(X), np.array(y)

def perform_linear_regression(X, y):
    # Add a column of ones to X to include the intercept term in the model
    X_b = np.c_[np.ones(X.shape[0]), X]
    
    # Compute the coefficients using the normal equation
    theta = np.linalg.inv(X_b.T @ X_b) @ X_b.T @ y
    
    # Extract coefficients
    intercept = theta[0]
    slopes = theta[1:]
    
    return intercept, slopes

def main():
    try:
        X, y = get_user_input()
        intercept, slopes = perform_linear_regression(X, y)
        
        print("Intercept:", intercept)
        print("Slopes:", slopes)
        
        # Compute predictions
        X_b = np.c_[np.ones(X.shape[0]), X]
        y_pred = X_b @ np.concatenate(([intercept], slopes))
        
        # Calculate Mean Squared Error and R^2 Score
        mse = np.mean((y - y_pred) ** 2)
        r2 = 1 - (np.sum((y - y_pred) ** 2) / np.sum((y - np.mean(y)) ** 2))
        
        print("Mean Squared Error:", mse)
        print("R^2 Score:", r2)
        
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()
