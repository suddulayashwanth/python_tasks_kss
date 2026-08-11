import numpy as np

random_values = np.random.random(8)

normalized_values = random_values * 100

filtered_values = normalized_values[normalized_values > 50]

sorted_values = np.sort(filtered_values)

print("Random values:", random_values)
print("Normalized values:", normalized_values)
print("Values greater than 50:", filtered_values)
print("Sorted filtered values:", sorted_values)