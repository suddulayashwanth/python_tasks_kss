import copy

employees = [[101, "A"], [102, "B"], [103, "C"]]

shallow_copy = copy.copy(employees)

employees[0][1] = "Z"

print("Original employees:", employees)
print("Shallow copy:", shallow_copy)

print("Both changed because nested lists are shared.")

employees = [[101, "A"], [102, "B"], [103, "C"]]

deep_copy = copy.deepcopy(employees)

employees[0][1] = "Z"

print("Original after modification:", employees)
print("Deep copy:", deep_copy)