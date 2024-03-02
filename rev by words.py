def reverse_by_words(str1):
  str_split=str1.split()
  print(str_split)
  res=str_split[::-1]
  print(res)
  return " ".join (res)
string=input("enter string:")
print(reverse_by_words(string))


'''
enter string:my name is yash
['my', 'name', 'is', 'yash']
['yash', 'is', 'name', 'my']
yash is name my ''
