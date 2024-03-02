# Input: nums = [1,2,3,4], k = 5
# Output: 2
# Explanation: Starting with nums = [1,2,3,4]:
# - Remove numbers 1 and 4, then nums = [2,3]
# - Remove numbers 2 and 3, then nums = []
# There are no more pairs that sum up to 5, hence a total of 2 operations.

def count_of_target(arr,k):
    count=0
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            if arr[i]+arr[j]==k:
                count+=1
    return count
#driver code
arr=list(map(int,input("Enter tha array:").split()))
k=int(input("Enter target:"))
print(count_of_target(arr,k))
 
