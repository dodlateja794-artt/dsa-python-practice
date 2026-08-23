nums = [2,3,1,2,4,3]
target=6
min_len=float('inf')
left=0
window_sum=0
for right in range(len(nums)):
    window_sum+=nums[right]
    while window_sum>=target:
        window_len=right-left+1
        min_len=min(min_len,window_len)
        window_sum-=nums[left]
        left+=1
print(min_len)

