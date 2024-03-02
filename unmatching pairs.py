def unmatching_pairs(str1):
    dict1={}
    for i in str1:
        if i not in dict1:
            dict1[i]=1
        else:
            dict1[i]+=1
    print(dict1)
    new=''
    for i,j in dict1.items():
        if j%2==1:
            new+=i
    return new
    
#driver code 
str1=input("Enter the string:")
res=unmatching_pairs(str1)
if res:
    print(res)
else:
    print(-1)


'''sample input=aabbccddc
    op= c
    because c is unpaired'''
