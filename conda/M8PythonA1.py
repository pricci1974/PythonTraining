import pandas as pd
import matplotlib.pyplot as plt

#This loads the spreadsheet into the dataframe
df = pd.read_csv("movies.csv")

#Decribes the program and output to the user
print("In this assignment, we will use a movie dataset obtained freely from Kaggle\n")
print("Pandas contains many helpful tools for working with data.\n")
print("Inspecting the data using the info() method in pandas.",
      "First, we will examine the various data elements in this set")
print(df.info())

print("\nThe info() function from pandas provides some basic summary statistics about the dataset")
print(df.describe())

print("\nThe head() function displays the first five entries")
print(df.head())

print("\nNext we will begin the cleaning process",
      "The isnull().sum() counts the instances of null values as follows:\n")
print(df.isnull().sum())

print("\nWe will use the dropna() function with a setting of inplace=true to remove and replace",
      "full rows that have and missing data\n")
df.dropna(inplace=True)

print("Reprint the number of rows with missing data to demonstrate the function worked!\n")
print(df.isnull().sum())

df['Decade'] = (df['year'] // 10) * 10 #Used to group the years into decades

yearly_avg = df.groupby('Decade')['rating'].mean() #Obtain average ratings

# Creates the plot
plt.figure(figsize=(8, 5))

# Creates the bar chart
plt.bar(yearly_avg.index.astype(str), yearly_avg.values, color='skyblue', edgecolor='navy')

# Add a global average line
plt.axhline(y=yearly_avg.mean(), color='red', linestyle='--', label='Overall Average Rating per Decade')

# Labels and Title
plt.xlabel('Year')
plt.ylabel('Average Rating')
plt.title('Average Numbers Per Decade')
plt.legend()

# Saves the chart as jpg because I use a remote server, I cannot use the show() function
plt.savefig("M8fig.jpg")

decade_counts = df.groupby(['Decade', 'year']).size().reset_index(name='count')
# Get the row with max count for each decade
best_years = decade_counts.loc[decade_counts.groupby('Decade')['count'].idxmax()]

# Plotting
plt.figure(figsize=(10, 6))
bars = plt.bar(best_years['year'].astype(str), best_years['count'], color='skyblue')

# Add Labels
plt.xlabel('Years with the Most Movies for Each Decade', fontsize=12)
plt.ylabel('Count', fontsize=12)
plt.title('Years with the Most Movies in Each Decade', fontsize=14)

# Notate the actual year
for bar, year in zip(bars, best_years['year']):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), 
             str(year), ha='center', va='bottom')

plt.savefig("M8fig2.jpg")