import numpy as np

values = np.array([10, 12, 15, 18, 100, 14, 13])

mean_value = np.mean(values)
standard_deviation = np.std(values)

lower_limit = mean_value - (2 * standard_deviation)
upper_limit = mean_value + (2 * standard_deviation)

filtered_values = values[
    (values >= lower_limit) &
    (values <= upper_limit)
]

print("Original values:", values)
print("Mean:", mean_value)
print("Standard deviation:", standard_deviation)
print("Lower limit:", lower_limit)
print("Upper limit:", upper_limit)
print("Values after removing outliers:", filtered_values)