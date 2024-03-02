arr = list(map(int,input("Enter:").split()))
dict1 = {}
for i in arr:
    if i  not in dict1:
        dict1[i]=1
    else:
        dict1[i]+=1
print(dict1)

mostelement = max(dict1,key=dict1.get)
most=dict1[mostelement]
print(f"{mostelement} occurs {most} times ")
