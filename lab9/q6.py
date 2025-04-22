def fun6():
    ls=[]
    n=int(input("Enter ending value"))
    for i in range(1,n+1):
        t=(i,i**2,i**3)
        tem=tuple(t)
        ls.append(tem)
    print(ls)

fun6()