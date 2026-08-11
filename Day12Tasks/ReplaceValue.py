import numpy as np

arr = np.array([5, 12, 18, 7, 25, 30])

arr[arr > 15] = 0

print("Updated array:", arr)