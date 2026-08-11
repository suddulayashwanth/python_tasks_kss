data = [[1, 2, 3], [4, 5], [6]]

flattened_list = [
    number
    for sublist in data
    for number in sublist
]

even_squares = [
    number ** 2
    for number in flattened_list
    if number % 2 == 0
]

print("Original data:", data)
print("Flattened list:", flattened_list)
print("Squares of even numbers:", even_squares)