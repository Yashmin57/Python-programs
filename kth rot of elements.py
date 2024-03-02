n= int(input("Enter no of inputs:"))
arr=list(map(int,input("enter:").split()))
target= int (input("Enter k:"))
for i in range (0,n):
    sum = (i+target)%n
    print(arr[sum])
