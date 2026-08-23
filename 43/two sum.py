arr = [2, 7, 11, 15]
target = 9
seen={}
for i in range(len(arr)):
    diff=target-arr[i]
    if diff in seen:
        print(seen[diff],i)
    seen[arr[i]]=i
    