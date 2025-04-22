def create_list(lst1: list,lst2: list):
    s1=set(lst1)
    s2=set(lst2)
    
    s3=s1.intersection(s2)
    lst3=list(s3)
    
    return lst3

lst1=list(map(int, input("Enter space-separated values of list1:").split()))
lst2=list(map(int, input("Enter space-separated values of list2:").split()))
print(create_list(lst1,lst2)) 