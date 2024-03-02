def findcons(str1):
    new=""
    vowels=['a','e','i','o','u']
    for i in str1:
        if i not in vowels:
            new += i
    return new
    
#driver code    
string=input("enter:")   
print(findcons(string))
            
