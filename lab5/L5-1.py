l1=[1,3,5,7,9]
l2=[2,4,6,8]

l1.insert(2,l2)
l1.pop(3)
ln=[]
print("final list is ", l1)
print(l1)
for i in l1:
    if(type(i)==list):
        ln.extend(i)
    else:
        ln.append(i)
    
print(ln)
