import numpy as np

class SimpleLinearRegression:
    def __init__(self, learning_rate=0.01, n_iterations=1000):
        
        self.learning_rate = learning_rate
        self.n_iterations = n_iterations
        # slope (m)
        self.weight = 0.0 
        # intercept (b)  
        self.bias = 0.0     

    def fit(self, X, y):
        # Convert to numpy arrays
        X = np.array(X)
        y = np.array(y)

        n_samples = len(X)

        # Gradient Descent
        for _ in range(self.n_iterations):
            # Predictions
            y_pred = self.weight * X + self.bias

            # Errors
            error = y_pred - y

            # Gradients
            dw = (2 / n_samples) * np.dot(X, error)
            db = (2 / n_samples) * np.sum(error)

            # Update parameters
            self.weight -= self.learning_rate * dw
            self.bias -= self.learning_rate * db

    def predict(self, X):
        X = np.array(X)
        return self.weight * X + self.bias

    def mse(self, X, y):
        y_pred = self.predict(X)
        return np.mean((y - y_pred) ** 2)
    