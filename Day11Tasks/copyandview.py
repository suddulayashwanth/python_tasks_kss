import numpy as np

original = np.array([10, 20, 30, 40])
copied_array = original.copy()

original[0] = 100

print("Copy example:")
print("Original:", original)
print("Copy:", copied_array)

original2 = np.array([10, 20, 30, 40])
viewed_array = original2.view()

original2[0] = 100

print("\nView example:")
print("Original:", original2)
print("View:", viewed_array)