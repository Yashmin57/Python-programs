#input: nums=[1,2,3,4]
#output: [24,12,8,6]

def productofarrexceptself(nums):
    pro=[]
    for i in range(len(nums)):
        res=1
        temp_arr=nums[:i] + nums[i+1:]
        for j in temp_arr:
            res*=j
        pro.append(res)
    return pro
#driver code
nums=list(map(int,input("Enter:").split()))
print(productofarrexceptself(nums))
