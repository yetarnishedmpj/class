tem_f=[85,56,96,85]
tem_c=[]
for num in range(len(tem_f)):
    tem_c.append(int(5/9*(tem_f[num]-32)))

print("temperature in Fahrenheit is= ",tem_f)
print("temperature in Celcius is= ",tem_c)