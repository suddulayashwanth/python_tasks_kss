import numpy as np

data = [12, 7, 25, 3, 18, 10]

data_array = np.array(data)
sorted_array = np.sort(data_array)
split_arrays = np.split(sorted_array, 2)

first_part = split_arrays[0]
second_part = split_arrays[1]

first_sum = np.sum(first_part)
second_sum = np.sum(second_part)

print("Sorted array:", sorted_array)
print("First split array:", first_part)
print("Second split array:", second_part)
print("Sum of first part:", first_sum)
print("Sum of second part:", second_sum)