import random
import math

number=random.randint(1,50)

for i in range(5):
    guess=int(input("Enter guess: "))
    if guess==number:
        print("Correct")
        break
    print("Difference:",math.fabs(number-guess))
else:
    print("Number was",number)