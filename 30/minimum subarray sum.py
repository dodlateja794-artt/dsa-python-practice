nums = [2,3,1,2,4,3]
target = 7
min_window=0
left=0
window_length=0
min_len=float('inf')
for right in range(len(nums)):
    min_window+=nums[right]
    while min_window>=target:
        window_length=right-left+1
        min_len=min(min_len,window_length)
        min_window-=nums[left]
        left+=1
print(min_len)