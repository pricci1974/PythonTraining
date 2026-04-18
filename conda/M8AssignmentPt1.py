import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# 1. Load data from CSV
# Replace 'data.csv' with your file path
df = pd.read_csv('bankdata.csv') 

# 2. Select features for clustering
# Example: Using 'Annual Income' and 'Spending Score' columns
X = df[['CreditScore', 'Balance']]

# 3. Feature Scaling (Crucial for distance-based algorithms like K-Means)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 4. Apply K-Means Clustering
# n_clusters is the number of groups you want to find
kmeans = KMeans(n_clusters=5, random_state=42)
df['Cluster'] = kmeans.fit_predict(X_scaled)

# 5. Visualize the results
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='CreditScore', y='Balance', 
                hue='Cluster', palette='viridis')
plt.title('Customer Segments')
plt.savefig('bankcluster.jpg')

# 6. Export results back to a CSV
df.to_csv('clustered_results.csv', index=False)
