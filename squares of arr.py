'''def square(arr):
  new=[]
  print(arr)
  for i in arr:
    re=i**2
    new.append(re)
  new.sort()
  return new
array=list(map(int,input("Enter:").split()))
print(square(array))'''

''''arr=[-4,-3,2,3,10]
sqr_arr= [i**2 for i in arr ]
print(sorted(sqr_arr))'''

arr=[-4,-3,2,3,10]
sqr_arr= [i**2 for i in arr ]
#print(sqr_arr.sort())
'''The issue here is similar to the previous one. The sort() method in Python sorts the list in place and returns None.
 So when you do print(sqr_arr.sort()), you're printing the result of sqr_arr.sort(), which is None.'''
sqr_arr.sort()
print(sqr_arr)
