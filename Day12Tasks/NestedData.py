import copy

classes = [
    ["Math", [30, 35]],
    ["Science", [25, 28]]
]

copied_classes = copy.deepcopy(classes)

classes[0][1][0] = 40

print("Modified original:", classes)
print("Deep copied data:", copied_classes)

print("The copied data is unchanged because deep copy creates independent objects.")