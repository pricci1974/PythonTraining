import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

# 1. Load CSV file
# Ensure 'Date' is the index and parsed as dates
df = pd.read_csv('weather.csv', nrows=500, parse_dates=['Date_Time'], index_col='Date_Time')
print(df.head())
# 2. Visualize data to check for trends
df.plot(figsize=(10, 5))
plt.title("Time Series Data")
plt.show()

# 3. Define and Fit ARIMA Model
# Example order (p=5, d=1, q=0) - these should be tuned for your data
model = ARIMA(df['Temperature_C'], order=(5, 1, 0))
model_fit = model.fit()

# 4. Print Summary and Plot Residuals
print(model_fit.summary())
model_fit.resid.plot(title="Residuals")
plt.savefig("model.jpg")

# 5. Forecast future values
forecast = model_fit.forecast(steps=10)
print("Forecasted Values:\n", forecast)
