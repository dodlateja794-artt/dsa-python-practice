nums = [2,4,6,8]
for i in range(len(nums)):
    if nums[i] > 4:
        nums.pop(i)
print(nums)
