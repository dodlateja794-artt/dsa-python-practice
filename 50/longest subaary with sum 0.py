nums = [15, -2, 2, -8, 1, 7, 10, 23]
seen={0:-1}
max_len=0
prefix_sum=0
for i in range(len(nums)):
    prefix_sum+=nums[i]
    if prefix_sum in seen:
        seen[prefix_sum]
