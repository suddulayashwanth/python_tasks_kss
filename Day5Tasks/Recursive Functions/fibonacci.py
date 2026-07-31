def fibonacci(n):
    if n<=1:
        return n
    return fibonacci(n-1)+fibonacci(n-2)

n=int(input("Enter number: "))
print(fibonacci(n))