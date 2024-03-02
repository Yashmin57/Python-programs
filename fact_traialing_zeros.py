
def fact(n):
    if(n==0) or (n==1):
        return 1
    else:
        return n*fact(n-1)

def trail(n):
    num=fact(n)
    new=str(num)
    new1=new.split('0')
    print(new1)
    count =0
    for i in reversed(new1):
        if i=='':
            count+=1
        else:
            break
    return count
    
#driver code
n= int(input("Enter a number:"))
print("Count of trailing zeros.....",trail(n))
        
        
    
