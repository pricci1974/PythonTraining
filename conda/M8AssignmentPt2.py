import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# 1. Load data from CSV
df = pd.read_csv('bankdata.csv')

# 2. Select feature (X) and target (y)
# X must be a 2D array, so we use double brackets
X = df[['HasCrCard']] 
y = df['Exited']

# 3. Create and train the model
model = LinearRegression()
model.fit(X, y)

# 4. Make a prediction (e.g., for 5 years of experience)
prediction = model.predict([[1]])
print(f"Predicted Customer: {prediction[0]}")

# 5. Visualize (Optional)
plt.scatter(X, y, color='blue')
plt.plot(X, model.predict(X), color='red')
plt.savefig("bankreg.jpg")
