import random
random_numbers=[]
for i in range(50):
    random_numbers.append(random.randint(1,30))
print("Original list with duplicates",random_numbers)
unique_numbers = []
for num in random_numbers:
    if num not in unique_numbers:  
        unique_numbers.append(num)
print("Final list",unique_numbers)
