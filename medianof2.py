
def medianof2(arr1,arr2):
    new=[]
    for i in arr1:
        new.append(i)
    for i in arr2:
        new.append(i)
    new.sort()
    
    mid =len(new)//2
    if len(new)%2==1:
        return new[mid]
    else:
        res=(new[mid]+new[mid-1])//2
        return res
#driver Code
arr1=list(map(int,input("enter arr1").split()))
arr2=list(map(int,input("enter arr2").split()))
result = medianof2(arr1,arr2)
print(f"{result:.5f}")
