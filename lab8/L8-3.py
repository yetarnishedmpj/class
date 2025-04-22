def q3():
    s=set()
    for i in range(5):
        name=input("Enter names to add in set:")
        s.add(name)

    print(s)
    mod=input("Enter name to modify in set:")
    s.remove(mod)
    new=input("Enter new name to modify in set:")
    s.add(new)

    del1=input("Enter first name to delete in set:")
    del2=input("Enter second name to delete in set:")
    s.remove(del1)
    s.remove(del2)

    print(s)
q3()