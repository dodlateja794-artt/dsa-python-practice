nums = [1, 2, 1, 2]
k=3
prefix_sum=0
count=0
seen={0:1}
for i in range(len(nums)):
    prefix_sum+=nums[i]
    current_sum=prefix_sum-k
    if current_sum in seen:
        count+=seen[current_sum]
    seen[prefix_sum]=seen.get(prefix_sum,0)+1
print(count)