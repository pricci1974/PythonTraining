import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report, ConfusionMatrixDisplay
import matplotlib.pyplot as plt
import numpy as np

# 1. Load the data from a CSV file
try:
    data = pd.read_csv('loanDefault.csv')
except FileNotFoundError:
    print("Error: The file was not found. Please check the file path.")
    exit()

# Display the first few rows 
print("Data loaded successfully:")
print(data.head())

# Define features and target 
feature_cols = ['Income', 'Age', 'Experience'] 
target_col = 'Risk_Flag' 

X = data[feature_cols] # Features
y = data[target_col]   # Target 

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42)

# Build logistic regression model
logreg = LogisticRegression(max_iter=1000)
logreg.fit(X_train, y_train)

# Make predictions on the test set
y_pred = logreg.predict(X_test)

# Generate the confusion matrix
cnf_matrix = confusion_matrix(y_test, y_pred)
print("\nConfusion Matrix (numpy array):")
print(cnf_matrix)

# Create classification report
report = classification_report(y_test, y_pred, zero_division=0.0)
print("\nClassification Report:")
print(report)

# Visualize the confusion matrix
disp = ConfusionMatrixDisplay(confusion_matrix=cnf_matrix, display_labels=logreg.classes_)
disp.plot()
plt.title('Confusion Matrix for Logistic Regression Model')
plt.savefig("myplot.jpg")

