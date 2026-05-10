import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

np.random.seed(42)
X=2*np.random.rand(100,1)
y=4+3*X+np.random.randn(100,1)

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

model=LinearRegression()

model.fit(X_train,y_train)

print("Coefficient(m):" ,model.coef_[0][0])
print("Intercept(b): ",model.intercept_[0])

y_pred=model.predict(X_test)

print("Actual values: ",y_test)
print("Predicted values: ",y_pred)

mean_squared_error=mean_squared_error(y_test,y_pred)
print("Mean Squared Error: ",mean_squared_error )

#Predict unseen data points
new_X=np.array([[1.5]])
predicted_y=model.predict(new_X)
print("Predicted output for X=1.5: ",predicted_y[0][0])







