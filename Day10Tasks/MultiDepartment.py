import numpy as np

branch_a = np.array([
    [10, 20],
    [30, 40]
])

branch_b = np.array([
    [5, 15],
    [25, 35]
])

combined_matrix = np.concatenate((branch_a, branch_b), axis=0)
total_employees = np.sum(combined_matrix)

print("Combined matrix:")
print(combined_matrix)

print("Total employees:", total_employees)