import numpy as np

salaries = np.array([25000, 40000, 15000, 50000, 30000])

condition = salaries > 30000

filtered_salaries = salaries[condition]
employee_count = np.count_nonzero(condition)

print("Salaries above 30000:", filtered_salaries)
print("Number of employees:", employee_count)