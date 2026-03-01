import math
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression 
from dmba import regressionSummary, classificationSummary  
from sklearn.metrics import r2_score

walmart_df = pd.read_csv('walmart.csv')

exclude_columns =('Weekly_Sales', 'Date', 'Holiday_Flag', 'Store',
                  'CPI', 'Temperature', 'Fuel_Price')

predictors = [s for s in walmart_df.columns if s not in exclude_columns] 

outcome = 'Weekly_Sales'

X = walmart_df[predictors]
y = walmart_df[outcome] 
train_X, valid_X, train_y, valid_y = train_test_split(X, y, test_size=0.4,
                                                       random_state=1)
reg = LinearRegression()
reg.fit(train_X, train_y)

# evaluate performance 

# # training
regressionSummary(train_y, reg.predict(train_X)) 
# validation
regressionSummary(valid_y, reg.predict(valid_X)) 


X_R2 = walmart_df[['Unemployment']]  # Use double brackets to keep it as a DataFrame
y_R2 = walmart_df['Weekly_Sales']

model = LinearRegression()
model.fit(X_R2, y_R2)

y_pred_R2 = model.predict(X_R2)

r2 = r2_score(y, y_pred_R2)

print("\n\nR Squared values - Unemployment on Weekly Sales\n")

print(f"R-squared value: {r2}")