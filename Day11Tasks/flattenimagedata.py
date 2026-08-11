import numpy as np

image_data = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

flattened_array = image_data.flatten()

print("Original image data:")
print(image_data)

print("Flattened array:", flattened_array)