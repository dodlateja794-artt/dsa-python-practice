nums = [3,3,4,2,3,3,3]
seen={}
for i in nums:
    if i in seen:
        seen[i]+=1
    else:
        seen[i]=1
for key,value in seen.items():
    if value>len(nums)//2:
        print(key)
    