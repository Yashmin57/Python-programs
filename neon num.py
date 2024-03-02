def neon(num):
  sum=0
  sq=str(num**2)
  for i in sq:
    bit=int(i)
    sum += bit
  if(sum==num):
    return True
  return False
n=int(input("enter no:"))
if (neon(n)):
  print("neon number")
else:
  print("not neon number")  

#example 
  # i/p : 9
  # o/p : neon (9^2= 81 ... 8+1=9)
