def generate_numbers(n):
    for number in range(1, n + 1):
        yield number


n = int(input("Enter N: "))

for value in generate_numbers(n):
    print(value)