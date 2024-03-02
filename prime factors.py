def find_factors(num):
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
    return factors

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

number1 = int(input("Enter a number: "))

factors = find_factors(number1)
prime_factors = [f for f in factors if is_prime(f)]

print("Prime factors of", number1, "are:", *prime_factors)
   #indha star dha unpacking operator
