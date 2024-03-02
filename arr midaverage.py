def midavg(arr):
    length= len(arr)
    mid= length//2
    first=arr[:mid]
    sec=arr[mid:]
    sum1= sum(first)
    sum2=sum(sec)
    avg1=sum1//len(first)
    avg2=sum2//len(sec)
    if avg1==avg2:
        return("Yes")
    else:
        return("No")
        
#driver code
arr=list(map(int,input("Enter:").split()))
print(midavg(arr))
