def q4():
    s=set()
    x=int(input("Enter no of values which you want to add:"))
    for i in range(x):
        ele=input("Enter name:")
        s.add(ele)
    a=set()
    b=set()
    for i in s:
        if (i[0]=='A' or i[0]=='a'):
            a.add(i)
        elif (i[0]=='B' or i[0]=='b'):
            b.add(i)
        else:
            pass
        
    print("vaues which starts with 'A'or'a'",a)
    print("vaues which starts with 'B'or'b'",b)
q4()