nums = [1, 2, 3, 4]
for i in range(len(nums)):
    nums[i] = nums[i] + nums[i+1]

print(nums)