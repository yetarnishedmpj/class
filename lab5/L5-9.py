import random
random_numbers1=[]
random_numbers2=[]
new = []
for i in range(20):
    random_numbers1.append(random.randint(1,20))
    random_numbers2.append(random.randint(1,20))
    
for num in random_numbers1:
    if random_numbers1[num] not in random_numbers2:
        new.append(random_numbers1[num])
print(random_numbers1)
print(random_numbers2)
print(new)