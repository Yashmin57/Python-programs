arr = list(map(int,input("Enter:").split()))
dict1 = {}
for i in arr:
    if i  not in dict1:
        dict1[i]=1
    else:
        dict1[i]+=1
print(dict1)
for ele,count in dict1.items():
    print(f" {ele} occured {count} times")
