nums = [4, 2, 1, 7, 8, 1, 2]
k = 3
left=0
curr_sum=0
max_sum=0
for right in range(len(nums)):
    curr_sum+=nums[right]
    window=right-left+1
    if window==k:
        max_sum=max(max_sum,curr_sum)
        curr_sum-=nums[left]
        left+=1
print(max_sum)