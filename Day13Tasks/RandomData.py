import numpy as np

nums = np.random.randint(1, 100, 10)

divisible_by_five = nums[nums % 5 == 0]

sorted_result = np.sort(divisible_by_five)

print("Random numbers:", nums)
print("Numbers divisible by 5:", divisible_by_five)
print("Sorted result:", sorted_result)