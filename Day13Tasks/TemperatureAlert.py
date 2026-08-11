import numpy as np

temps = np.array([28, 32, 35, 31, 29, 40, 38])

indices = np.where(temps > 30)[0]

print("Temperatures:", temps)
print("Indices where temperature is greater than 30:", indices)
print("Temperatures greater than 30:", temps[indices])