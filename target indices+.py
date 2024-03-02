
listarray = []
target = int(input("enter target:"))
n = int(input("numberof inputs"))
for i in range(n):
    element = int(input("enter element:"))
    listarray.append(element)
for i in range(n):
            for j in range (i+1 ,n ):
                        if listarray[i]+listarray[j]==target:
                          print(i,j)
            
                
