nums = [-2,1,-3,4,-1,2,1,-5,4]
window_sum=nums[0]
max_sum=window_sum
for i in range(1,len(nums)):
    window_sum=max(nums[i],window_sum+nums[i])
    max_sum=max(window_sum,max_sum)
print(max_sum)