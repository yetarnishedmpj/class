# Task 2: Add corresponding elements of two lists using map and lambda
list1 = [1, 2, 3, 4, 5, 6]
list2 = [6, 5, 4, 3, 2, 1]
result = list(map(lambda x, y: x + y, list1, list2))
print("Sum of corresponding elements:", result)