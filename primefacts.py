def find_factors(n):
    factors=[]
    for i  in range (1,n+1):
        if n%i==0:
            factors.append(i)
    return factors
def isprime(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
    
#driver code
n = int(input("Enter a number:"))
res=find_factors(n)
prime_facts=[f for f in res if isprime(f)]
print(prime_facts)
#print(f" prime factors are...{*prime_facts}")
