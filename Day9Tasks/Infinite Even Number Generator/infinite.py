def even_number_generator():
    number = 2

    while True:
        yield number
        number += 2


n = int(input("Enter how many even numbers you want: "))
generator = even_number_generator()

for i in range(n):
    print(next(generator))