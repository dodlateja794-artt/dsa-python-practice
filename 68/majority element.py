nums = [2, 2, 1, 1, 2, 2, 3]
n=7
seen={}
for i in nums:
    if i in seen:
        seen[i]+=1
    else:
        seen[i]=1
for key,value in seen.items():
    if n//2<value:
        print(key)