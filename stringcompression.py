def stringcompression(str1):
    new_list=[]
    dict1={}
    for i in str1:
        if i not in dict1:
            dict1[i]=1
        else:
            dict1[i]+=1
    #print(dict1)
    for ele,count in dict1.items():
        if count>1:
            new_list.append(ele)
            if count>10:
                ft=count//10
                new_list.append(str(ft))
                se=count%10
                new_list.append(str(se))
            else:
                new_list.append(str(count))
        else:
            new_list.append(ele)
    return new_list
    #return len(new_list)
#driver code
str1=list(map(str,input("Enter:").split()))
res=stringcompression(str1)
print(res)
print(len(res))




    
'''Example 1:

Input: chars = ["a","a","b","b","c","c","c"]
Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".
Example 2:

Input: chars = ["a"]
Output: Return 1, and the first character of the input array should be: ["a"]
Explanation: The only group is "a", which remains uncompressed since it's a single character.
Example 3:

Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".'''
    
    
    
    
    
    

