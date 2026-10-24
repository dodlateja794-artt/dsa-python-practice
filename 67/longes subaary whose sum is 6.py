nums = [1, 2, 3, -2, 5, -3]
target = 6
seen={0:-1}
prefix_sum=0
max_len=0
for i in range(len(nums)):
    prefix_sum+=nums[i]
    current_sum=prefix_sum-target
    if current_sum in seen:
        length=i-seen[current_sum]
        max_len=max(length,max_len)
    if prefix_sum not in seen:
        seen[prefix_sum]=i
print(max_len)