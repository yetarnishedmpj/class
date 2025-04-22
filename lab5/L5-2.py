import random
n=[]
for i in range(20):
    n.append(random.randint(0,50))
print(n)
new=[]
m=int(input("Enter your number"))

positions = [index for index, value in enumerate(n) if value == m]

if positions:
    print(f"The number {m} is found at positions: {positions}")
else:
    print(f"The number {m} is not in the list.")