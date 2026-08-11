import numpy as np

defect_codes = np.array([2, 4, 1, 4, 3, 4, 5])
indexes = np.where(defect_codes == 4)[0]

print("Indexes containing value 4:", indexes)