num = int(input("Enter the number: "))
a, b = 0, 1
print(a, b, end=" ")

for i in range(3, num + 1):
    c = a + b
    a=b
    b=c
    print(c, end=" ")
