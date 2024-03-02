'''def leftrotate(arr, k):
    for i in range(k):
        arr1=arr
        arr1.append(arr1.pop(0))
    return arr1

def rightrotate(arr, k):
    res = arr[-k:] + arr[:-k]
    return res

# driver code
arr = list(map(int, input("enter: ").split()))
k = int(input("Enter k: "))
rotated_arr = rightrotate(arr, k)
print("right rotate:")
print(rotated_arr)
res =leftrotate(arr, k)
print("left rotate:")
print(res)''''

def rotate (arr,k,n):
    if(n=="left"):
        res = arr[k:] + arr[:k]
        return res
    else:
        res = arr[-k:] + arr[:-k]
        return res

arr = list(map(int, input("enter: ").split()))
k = int(input("Enter k: "))
n = input("Enter left or right:")
result= rotate(arr,k,n)
for i in result:
    print(i,end =" ")
