def count_lower_upper(a:str):
    uppercase=0
    lowercase=0
    for i in a:
        if(i.isupper()):
            uppercase+=1
        else:
            lowercase+=1
    dic={f"upper":{uppercase},"lower":{lowercase}}
    print(dic)

count_lower_upper("Rudra")