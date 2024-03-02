def letryt(arr,k,n):
    if(n=='left'):
        res=arr[k:] + arr[:k]
        return res
    else:
          res=arr[-k:] + arr[:-k]
          return res

arr=list(map(int,input("enter the array:").split()))
print(arr)
k=int(input("enter the k value:"))
n=input("enter the left or right")
print(*letryt(arr,k,n))
        
