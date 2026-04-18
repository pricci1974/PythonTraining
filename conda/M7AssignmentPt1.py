import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import STL


# 1. Load the dataset
# Ensure your CSV has a date column and a value column (e.g., 'date' and 'sales')
df = pd.read_csv('weather.csv', nrows=1000, parse_dates=['Date_Time'], index_col='Date_Time')

# 2. Set frequency (Required for decomposition)
# Use 'D' for Daily, 'MS' for Monthly Start, etc.
print(df.head(5))
df = df.asfreq('MS') 

# 3. Perform Decomposition
# 'additive' is for linear trends; 'multiplicative' for exponential trends

stl = STL(df['Temperature_C'], seasonal=7)
result = stl.fit()
# 4. Plot the results
result.plot()
plt.savefig("Weather.jpg")
