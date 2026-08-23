arr=[1,2,3,4]
target=7
seen={}
for i in range(len(arr)):
    diff=target-arr[i]
    if diff in seen:
        print(seen[diff],i)
    seen[arr[i]]=i