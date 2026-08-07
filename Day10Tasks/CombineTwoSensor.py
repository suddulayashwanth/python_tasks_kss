import numpy as np

sensor1 = np.array([10, 20, 30])
sensor2 = np.array([40, 50, 60])

combined_readings = np.concatenate((sensor1, sensor2))

print("Sensor 1:", sensor1)
print("Sensor 2:", sensor2)
print("Combined readings:", combined_readings)