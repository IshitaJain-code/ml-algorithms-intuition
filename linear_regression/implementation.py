import numpy as np
from sklearn.model_selection import train_test_split

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
    
np.random.seed(42)
X=2*np.random.rand(100)    
y=4+X+np.random.randn(100)

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
    
model=SimpleLinearRegression(learning_rate=0.01,n_iterations=1000)

model.fit(X_train,y_train)

print("Coefficient(m): ",model.weight)
print("Intercept(b): ",model.bias)

y_predict=model.predict(X_test)

print("\nFirst 5 Actual values: ",y_test[:5])

print("\nFirst 5 Predicted values: ",y_predict[:5])

mse=model.mse(X_test,y_test)
print("\nMean Squared Error: ",mse)

#Predict unseen data points
new_X=[1.5]
predicted_y=model.predict(new_X)
print("Predicted output for X=1.5: ",predicted_y)



