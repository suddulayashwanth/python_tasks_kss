import numpy as np

data = np.array([1, 2, 2, 3, 1, 4, 2, 3])

unique_numbers, counts = np.unique(data, return_counts=True)

print("Unique numbers:", unique_numbers)
print("Counts:", counts)

print("Numbers with their counts:")

for number, count in zip(unique_numbers, counts):
    print(number, "appears", count, "times")