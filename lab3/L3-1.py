def q1():
    string=input("Enter string to check: ")
    count=0
    for char in string:
            if char in "aeiouAEIOU":
                count+=1
    count=string.count("u")
    print("No of given vovel is ",count)
q1()
