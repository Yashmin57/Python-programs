num = int(input("Enter a number: "))
list1 = str(num)
ans = 0
for i in range(len(list1)-1):
    ans += int(list1[i]) ** int(list1[i + 1])
ans += int(list1[-1]) ** int(list1[0])
print(ans)
