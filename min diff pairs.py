n = int(input("Enter the array size: "))
listarr = []
for i in range(n):
    element = int(input("enter element:"))
    listarr.append(element)

# Sorting the array

sortedarr= sorted(listarr)

# Finding the minimum difference
min_diff = sortedarr[1] - sortedarr[0]
for i in range(1, n):
    if sortedarr[i] - sortedarr[i - 1] <= min_diff:
        min_diff = sortedarr[i] -sortedarr[i - 1]

# Printing the pairs with minimum difference
for i in range(1, n):
    if sortedarr[i] - sortedarr[i - 1] == min_diff:
        print(sortedarr[i - 1], sortedarr[i], end=' ')
