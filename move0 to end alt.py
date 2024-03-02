'''def move_zero_toend(arr,n):
    j=0
    for i  in range(n):
        if arr[i] !=0:
            arr[i] , arr[j] = arr[j] , arr[i]
            j+=1

#driver code
arr = list(map(int,input("Enter :").split()))
n =  len (arr)
move_zero_toend(arr,n)
print("Array after pushing zeros to the end:")
print(arr)'''




def move0toend(arr,n):
    for i in arr:
        if i==0:
            arr.remove(i)
            arr.append(i)
#driver code
arr = list(map(int,input("Enter :").split()))
n =  len (arr)
move0toend(arr,n)
print("Array after pushing zeros to the end:")
print(arr)            
    
