l = [("20",), ("85",), "Alice",(),"Roshni", ("50",), "kriti",12,17,5,7,"Rishi", ("24",),(),[]]
# for ele in len(l):
#     if len(l[ele]) == 0:
#         l.pop(ele)  
# l = [i for i in l if i]
# print(l)
for i in l:
    if type(i) == tuple and len(i) == 0:
        l.remove(i)
print(l)