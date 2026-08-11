import numpy as np

sales = np.array([12000, 18000, 9000, 22000, 15000, 30000])

average_sales = np.mean(sales)

filtered_sales = sales[sales > average_sales]

print("Sales:", sales)
print("Average sales:", average_sales)
print("Sales greater than average:", filtered_sales)