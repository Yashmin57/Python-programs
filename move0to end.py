def movezeros_to_end(arr,n):
    count =0    
    for i in range (n):
        if arr[i]!= 0 :
            arr[count] = arr[i]
            count +=1
    # Now all non-zero elements have been
    # shifted to front and 'count' is set
    # as index of first 0. Make all
    # elements 0 from count to end. 

    while (count<n):
        arr[count]=0
        count+=1

#driver code
arr = list(map(int,input("Enter :").split()))
n =  len (arr)
movezeros_to_end(arr,n)
print("Array after pushing zeros to the end:")
print(arr)
