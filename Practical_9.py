import numpy as np
import pandas as pd

# NumPy array operations
array1 = np.array([1, 2, 3, 4, 5])
array2 = np.array([10, 20, 30, 40, 50])

# Element-wise addition
sum_array = np.add(array1, array2)
# Modified print statement
print("Sum of arrays:", sum_array)

# Element-wise multiplication
product_array = np.multiply(array1, array2)
# Modified print statement
print("Product of arrays:", product_array)

# Pandas DataFrame operations
data = {
    'A': [1, 2, 3, 4, 5],
    'B': [10, 20, 30, 40, 50]
}
df = pd.DataFrame(data)

# Adding a new column
df['C'] = df['A'] + df['B']
# Modified print statement
print("\nDataFrame with new column:\n", df)

# Dropping a column
df = df.drop(columns=['C'])
# Modified print statement
print("\nDataFrame after dropping column 'C':\n", df)

# Descriptive statistics
# Modified print statement
print("\nDescriptive statistics:\n", df.describe())

'''
# Output:

Sum of arrays: [11 22 33 44 55]
Product of arrays: [ 10  40  90 160 250]

DataFrame with new column:
   A   B   C
0  1  10  11
1  2  20  22
2  3  30  33
3  4  40  44
4  5  50  55

DataFrame after dropping column 'C':
   A   B
0  1  10
1  2  20
2  3  30
3  4  40
4  5  50

Descriptive statistics:
               A          B
count  5.000000   5.000000
mean   3.000000  30.000000
std    1.581139  15.811388
min    1.000000  10.000000
25%    2.000000  20.000000
50%    3.000000  30.000000
75%    4.000000  40.000000
max    5.000000  50.000000
'''