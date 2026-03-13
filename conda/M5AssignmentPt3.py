import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder

# 1. Load the CSV data
# Replace 'your_data.csv' with the path to your actual file
try:
    df = pd.read_csv('loanDefault.csv')
except FileNotFoundError:
    print("Error: 'your_data.csv' not found. Please check the file path.")
    exit()

# 2. Data Preparation (Handle missing values and categorical data)
# Drop rows with missing target values (adjust 'target_column_name' as needed)
df.drop(columns=['Married/Single', 'House_Ownership', 'Car_Ownership', 'Profession', 'CITY', 'STATE'], inplace=True)
print("Original DataFrame:")
print(df.head())

# Select features and target (adjust column names)
feature_columns = ['Income', 'Age', 'Experience'] # List of your feature column names
target_column = 'Risk_Flag' # Name of your target column

X = df[feature_columns]
y = df[target_column]

# Convert categorical data to numerical if needed (using LabelEncoder for the target)
if y.dtype == 'object':
    le = LabelEncoder()
    y = le.fit_transform(y)

# For features, one-hot encoding with pandas.get_dummies might be better for some columns
# X = pd.get_dummies(X, columns=['categorical_feature_name'])

# 3. Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42) # 80% train, 20% test

# 4. Create and train the Random Forest model
# n_estimators is the number of trees in the forest (100 is a common default)
rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)
rf_classifier.fit(X_train, y_train)

# 5. Make predictions on the test data
y_pred = rf_classifier.predict(X_test)

# 6. Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.2f}")

# 7. (Optional) Save predictions to a new CSV file
predictions_df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
predictions_df.to_csv('predictions.csv', index=False) #
