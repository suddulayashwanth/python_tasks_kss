import numpy as np

sales = np.array([
    10, 20, 30, 40, 50, 60,
    70, 80, 90, 100, 110, 120
])

sales_matrix = sales.reshape(4, 3)

print("4 x 3 sales matrix:")
print(sales_matrix)