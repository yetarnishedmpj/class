d = {
    "dept1":{1:2000,2:6580,3:4576},
    "dept2":{1:1000,2:8580,3:9576},
    "dept3":{1:4000,2:2580,3:3576}
}
for i in d:
    print("Department:",i)
    print("Minimum salary:",min(d[i].values()))
    print("Maximum salary:",max(d[i].values()))
    print()