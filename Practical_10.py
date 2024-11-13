import numpy as np

import matplotlib.pyplot as plt

# Line plot
x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.figure(figsize=(10, 6))
plt.subplot(2, 3, 1)
plt.plot(x, y, label='sin(x)')
plt.title('Line Plot')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.legend()

# Bar graph
categories = ['A', 'B', 'C', 'D']
values = [3, 7, 5, 12]

plt.subplot(2, 3, 2)
plt.bar(categories, values, color='blue')
plt.title('Bar Graph')
plt.xlabel('Categories')
plt.ylabel('Values')

# Histogram
data = np.random.randn(1000)

plt.subplot(2, 3, 3)
plt.hist(data, bins=30, color='green', edgecolor='black')
plt.title('Histogram')
plt.xlabel('Value')
plt.ylabel('Frequency')

# Scatter plot
x = np.random.rand(100)
y = np.random.rand(100)

plt.subplot(2, 3, 4)
plt.scatter(x, y, color='red')
plt.title('Scatter Plot')
plt.xlabel('x')
plt.ylabel('y')

# Pie chart
sizes = [15, 30, 45, 10]
labels = ['A', 'B', 'C', 'D']
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0.1, 0, 0, 0)  # explode 1st slice

plt.subplot(2, 3, 5)
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.title('Pie Chart')

plt.tight_layout()
plt.show()