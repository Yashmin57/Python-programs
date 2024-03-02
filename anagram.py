def anagram(str1,str2):
    new_str1=list(sorted(str1))
    new_str2=list(sorted(str2))
    if len(new_str1)==len(new_str2):
        if new_str1==new_str2:
            return True
    else:
        return False
#driver code    
string1=input("enter:")
string2=input("enter:")
if (anagram(string1,string2)):
    print("anagram")
else:
    print("not anagram")
