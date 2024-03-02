import math
def isprime(n):
    fact=0
    if(n<=1):  return False
    for i in range (1,n+1):
        if n%i==0:
             fact+=1
    if (fact==2):
        return True
    else:
        return False

#driver code
n = int(input("Enter range:"))
for i in range(1,n+1):
              if(isprime(i)):
                 print(i, end=" ")
              
