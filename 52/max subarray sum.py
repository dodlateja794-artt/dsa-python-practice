nums = [2, 1, 5, 1, 3, 2]
k = 3
curr_sum=0
max_sum=0
left=0
for right in range(len(nums)):
    curr_sum+=nums[right]
    max_window=right-left+1
    if max_window==k:
        max_sum=max(curr_sum,max_sum)
        curr_sum-=nums[left]
        left+=1
print(max_sum)