import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

# --- 1. Load the CSV Data ---
# Use pandas to read the CSV file into a DataFrame
df = pd.read_csv("loanDefault.csv", nrows=100)
df.drop(columns=['Married/Single', 'House_Ownership', 'Car_Ownership', 'Profession', 'CITY', 'STATE'], inplace=True)
print("Original DataFrame:")
print(df.head())

# --- 2. Data Preprocessing (Handle Categorical Variables) ---
# Decision trees in scikit-learn work best with numerical data. 
# We need to convert categorical columns ('Nationality' and 'Go') to numbers.


# --- 3. Split Data into Features (X) and Target (y) ---
# 'features' are the columns used to make a decision
features = ['Income', 'Age', 'Experience', 'CURRENT_JOB_YRS']
X = df[features] 
# 'y' is the target variable we want to predict
y = df['Risk_Flag'] 

# Optional: Split data into training and testing sets (useful for larger datasets)
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# --- 4. Train the Decision Tree Model ---
# Initialize the Decision Tree Classifier from scikit-learn
dtree = DecisionTreeClassifier(max_depth=5)

# Fit the model to the data
dtree = dtree.fit(X, y)

# --- 5. Make a Prediction ---
# Predict if a 40-year-old with 10 years experience, rank 8, from the UK (0) will 'Go' (1/YES)
prediction = dtree.predict([[50000, 40, 8, 10]])
print(f"\nPrediction for new data [100000, 40, 8, 10]: {prediction}") 

# --- 6. Visualize the Decision Tree (Optional) ---
plt.figure(figsize=(12,8))
plot_tree(dtree, feature_names=features, class_names=['NO', 'YES'], filled=True, rounded=True)
plt.title("Decision Tree Visualization")
plt.savefig("m5pt2.jpg")