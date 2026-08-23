arr=[2,7,4,5]
target=11
seen={}
for i in range(len(arr)):
    diff=target-arr[i]
    if diff in seen:
        print(seen[diff],i)
    seen[arr[i]]=i