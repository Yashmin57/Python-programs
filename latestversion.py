arr=["fle_1","fle_3","fle_2"]
#arr=[]
n=len(arr)
if n==0:
    print(-1)
else:
    latest=0
    for i in arr:
        if i.startswith("fle_") and i[4:].isdigit():
            version=int(i[-1])
            latest=max(latest,version)
    print(latest)
