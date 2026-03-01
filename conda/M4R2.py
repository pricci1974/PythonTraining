import math
import pandas as pd
from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression 


walmart_df = pd.read_csv('walmart.csv')

X = walmart_df[['Unemployment']]  # Use double brackets to keep it as a DataFrame
y = walmart_df['Weekly_Sales']

model = LinearRegression()
model.fit(X, y)

y_pred = model.predict(X)

r2 = r2_score(y, y_pred)

print("R Squared values - Unemployment on Weekly Sales")
print(f"Predicted values (first 5): {y_pred[:5]}")
print(f"R-squared value: {r2}")