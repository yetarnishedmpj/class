import random
random_numbers=[]
for i in range(30):
    random_numbers.append(random.randint(-10,20))
print("20 random numbers are",random_numbers)
positive_num = []
negative_num = []
for num in random_numbers:
    if num >= 0:
        positive_num.append(num)
    else:
        negative_num.append(num)
print("Positive numbers are",positive_num)
print("Negative numbers are",negative_num)