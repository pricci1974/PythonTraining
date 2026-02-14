import matplotlib.pyplot as plt
import numpy as np

# Sample data: two arrays of the same length
x = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6])
y = np.array([99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86])

# Create the scatter plot
plt.scatter(x, y)

# Add labels and a title for clarity (optional)
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.title('Simple Scatter Plot')

# Display the plot
plt.savefig("myplot.jpg")