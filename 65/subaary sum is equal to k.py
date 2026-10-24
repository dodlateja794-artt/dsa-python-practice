nums = [1, 2, 3, -2, 5]
k = 5
seen={0:1}
count=0
currnt_sum=0
for i in range(len(nums)):
    currnt_sum+=nums[i]
    prefix_sum=currnt_sum-k
    if prefix_sum in seen:
        count+=seen[prefix_sum]
    seen[currnt_sum]=seen.get(count,0)+1
print(count)
        
    