import random
import math

numbers=[]
for i in range(20):
    numbers.append(random.randint(1,200))

print(numbers)
print(max(numbers))
print(min(numbers))
print(math.sqrt(max(numbers)))
print(math.log(min(numbers)))