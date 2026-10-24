nums = [4, 5, 1, 2, 1, 4, 5]
seen={}
for i in nums:
    if i in seen:
        seen[i]+=1
    else:
        seen[i]=1
for key,values in seen.items():
    if values==1:
        print(key)