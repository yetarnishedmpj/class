d1 = {"Moong dal":89,"Chana dal":99,"Wheat":20}
d2 = {"Moong dal":2,"Chana dal":4,"Wheat":5}

final_bill = 0
for i in d1.keys():
    final_bill+=d1[i]*d2[i]
    
print("Your total bill is",final_bill)