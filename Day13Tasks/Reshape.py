import numpy as np

data = np.arange(1, 13)

matrix = data.reshape(3, 4)

row_averages = np.mean(matrix, axis=1)

print("Original data:", data)

print("3 x 4 matrix:")
print(matrix)

print("Average of each row:", row_averages)