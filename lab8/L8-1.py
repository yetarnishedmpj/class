def q1():
    l1 = ["rudra","maharshi","tanmay","ronit","yug"]
    l2=[]
    for i in range(len(l1)):
        l2.append(l1[i].upper())

    s2=set(l2)
    print(s2)
q1()