nums=[1,2,3,-1,-2]
k=3
prefix_sum=0
seen={0:1}
count=0
for i in range(len(nums)):
    prefix_sum+=nums[i]
    if prefix_sum-k in seen:
        count+=seen[prefix_sum-k]
    if prefix_sum in seen:
        seen[prefix_sum]+=1
    else:
        seen[prefix_sum]=1
print(count)

