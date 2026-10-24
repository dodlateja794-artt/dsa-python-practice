nums = [2, 2, 1, 1, 1, 2, 2]
seen={}
n=7
for i in nums:
    if i in seen:
        seen[i]+=1
    else:
        seen[i]=1
for key,value in seen.items():
    if value>n/2:
        print(key)