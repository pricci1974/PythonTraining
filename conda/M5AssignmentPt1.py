import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import MinMaxScaler

# 1. Load the data from a CSV file
# Replace 'your_data.csv' with the path to your actual CSV file.
# The data should be purely numerical for KNN. You may need to encode categorical data first.
try:
    df = pd.read_csv('loanDefault.csv')
except FileNotFoundError:
    print("Error: your_data.csv not found. Please check the file path.")
    exit()

# Display the first few rows and column names to verify


# 2. Prepare the features (X) and target (y) variables
# Replace 'target_column_name' and 'feature_column_1', 'feature_column_2', etc.,
# with your actual column names. The target is what you want to predict.
df.drop(columns=['Married/Single', 'House_Ownership', 'Car_Ownership', 'Profession', 'CITY', 'STATE'], inplace=True)
X = df.drop(['Risk_Flag', 'Experience'], axis=1) # Features
y = df['Risk_Flag']               # Target variable
print("Column names:", df.columns.values)
print(df.head())
# 3. Preprocess the data (Scaling is highly recommended for KNN)
# KNN uses distance metrics, so features should be on a similar scale.
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

# 4. Split the data into training and testing sets
# The data is typically split 80/20 or 70/30 for training/testing.
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)

# 5. Create and train the KNN model
# Choose a value for 'n_neighbors' (k). A common approach is to use the elbow method to find the best K value.
k_value = int(input("Input k value: ")) # Example value for K
knn = KNeighborsClassifier(n_neighbors=k_value)
knn.fit(X_train, y_train)

# 6. Make predictions on the test set
y_pred = knn.predict(X_test)

# 7. Evaluate the model's accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"\nModel Accuracy with K={k_value}: {accuracy:.2f}")

# 8. Use the trained model to predict a new data point
# Example of a single new data point (make sure it's scaled using the same scaler)
# new_point_data = [[feature1_val, feature2_val, ...]]
# new_point_scaled = scaler.transform(new_point_data)
# prediction = knn.predict(new_point_scaled)
# print(f"Prediction for new point: {prediction[0]}")
