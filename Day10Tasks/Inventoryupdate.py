import numpy as np

data = np.array([5, 10, 15, 20, 25, 30])

split_arrays = np.split(data, 3)

print("Original data:", data)

print("Processor 1:", split_arrays[0])
print("Processor 2:", split_arrays[1])
print("Processor 3:", split_arrays[2])