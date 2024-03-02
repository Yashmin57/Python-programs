arr = list(map(int,input("Enter:").split()))
min = float('inf')
max = float('-inf')
for  i in arr:
    if i>max:
        max=i    
    if i<min:
         min=i
print(f"maximum element is {max}")
print(f"minimum element is {min}")
      

              
