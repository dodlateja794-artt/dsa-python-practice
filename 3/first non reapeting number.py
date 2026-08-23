arr=[2,3,4,2,3,4,5]
seen={}
for num in arr:
    if num in seen:
        seen[num]+=1
    else:
        seen[num]=1
for num in arr:
    if seen[num]==1:
        print(num)
        break