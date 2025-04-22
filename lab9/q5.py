def ispangram(stat:str):
    s=set(stat)
    new=set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
    for stat in new:
        if set(stat) <= new:
            pass
        else:
            return False
    return True
    
ans1=ispangram("The quick brown fox jumps over the lazy dog")
print(ans1)
ans2=ispangram("Crazy Fredrick bought many very exquisite opal jewels")
print(ans2)