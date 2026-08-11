import numpy as np

sales = np.random.randint(100, 501, size=10)

average_sales = np.mean(sales)

print("Sales for 10 days:", sales)
print("Average sales:", average_sales)