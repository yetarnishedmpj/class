string = []
for num in range(5):
    string.append(input("Enter your string: "))
print("your original string is =",string)
new_string = []
for num in range(5):
    tem =string[num].upper()
    new_string.append(tem)
print("your new string is =",new_string)

