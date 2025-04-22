data = [("20",), ("85",), "Alice", "Roshni", ("50",), "kriti",12,17,5,7,"Rishi", ("24",)]
roll_no = []
name = []
age = []
print(data)

for ele in data:
    if isinstance(ele, tuple):
        roll_no.append(ele)
    elif isinstance(ele, str):
        name.append(ele)
    else:
        age.append(ele)
print(roll_no)
print(name)
print(age)