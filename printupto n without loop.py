'''def printwithoutloop(start,end):
  if start<=end:
    print(start, end =" ")
    printwithoutloop(start+1,end)
  
#driver code
start=int(input("Enter the starting number"))
end=int(input("Enter the ending number"))
print(f"The numbers between {start} and {end} are.....")
printwithoutloop(start,end)'''

numbers= range(1,101)
list(map(print,numbers ))
