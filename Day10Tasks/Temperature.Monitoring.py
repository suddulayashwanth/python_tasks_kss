import numpy as np

temperatures = np.array([
    [30, 32, 31],
    [29, 33, 34]
])

total_temperature = np.sum(temperatures)

print("Temperature array:")
print(temperatures)

print("Total temperature:", total_temperature)