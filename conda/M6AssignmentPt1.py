import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# 1. Load your CSV file
df = pd.read_csv('loanDefault.csv', nrows=500)

# 2. Select relevant numeric columns for clustering
# Replace 'Col1' and 'Col2' with your actual column names
data = df[['Income', 'Age']]

# 3. Scale the data (crucial for K-Means performance)
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)

# 4. Initialize and fit the K-Means model
# n_clusters is the number of groups you want to find
kmeans = KMeans(n_clusters=3, random_state=42)
df['Cluster'] = kmeans.fit_predict(scaled_data)

# 5. View results
print(df.head())

# Optional: Visualize the clusters
plt.scatter(df['Income'], df['Age'], c=df['Cluster'], cmap='viridis')
plt.title('K-Means Clustering Results')
plt.savefig('M7Fig.jpg')
