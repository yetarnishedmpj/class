def q2():
    import random
    s=set()
    count=0
    while(len(s)<=10):
        
        m=random.randint(15,45)
        if m in s:
            continue
        else:
            s.add(m)
    print(s)
    
    for ele in s.copy():
        if ele<30:
            count+=1
        else:
            pass
        
        if ele>35:
            s.discard(ele)
    print("No of values which are less than 30 is",count)
    print(s)
q2()