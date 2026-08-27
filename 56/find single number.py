nums = [4, 4, 2, 1, 2]
seen={}
for i in nums:
    if i in seen:
        seen[i]+=1
    else:
        seen[i]=1
for key,value in seen.items():
    if value==1:
        print(key)