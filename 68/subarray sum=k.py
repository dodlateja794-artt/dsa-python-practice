nums = [1, 2, 3, -2, 5]
k = 5
seen={0:-1}
max_sum=0
for i in range(len(nums)):
    prefix_sum+=nums[i]
    if prefix_sum-k in seen:
        seen[prefix_sum]+=1
    else:
        seen[prefix_sum]=1