import numpy as np

matrix = np.random.randint(0, 51, size=(3, 3))

filtered_values = matrix[matrix > 25]

print("Random 3 x 3 matrix:")
print(matrix)

print("Values greater than 25:")
print(filtered_values)