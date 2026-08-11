import numpy as np

temperatures = np.array([28, 31, 35, 27, 40, 22])
high_temperatures = temperatures[temperatures > 30]

print("Temperatures above 30:", high_temperatures)