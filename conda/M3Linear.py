import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import numpy as np

#data set
df = pd.read_csv("walmart.csv")

# Define independent variables (X) and dependent variable (y)
X = df[['Temperature']] 
y = df['Weekly_Sales'] 

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create model
model = LinearRegression()
# Fit the model using the training data (or all data if not splitting)
model.fit(X_train, y_train)

# Create predictions on the test data
predictions = model.predict(X_test)

# Calculate the MSE
mse_value = mean_squared_error(y_test, predictions)

print(f"Predicted values: {predictions.flatten()}")

print(f"Mean Squared Error (MSE): {mse_value:.2f}")

# Obtain and display results 
print(f"Intercept: {model.intercept_}")
print(f"Coefficients: {model.coef_}")

# Predict a new sales amount based on 75F temperature
predicted_results = model.predict([[75]])
print(f"Predicted Sales when Temperature is 75 F: {predicted_results}")