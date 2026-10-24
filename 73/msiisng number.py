nums=[-1, 4, 3, 1]
for i in range(len(nums)):
    while nums[i]>0 and nums[i]<=len(nums) and nums[i]!=nums[nums[i]-1]:
        correct_index=nums[i]-1
        nums[i],nums[correct_index]=nums[correct_index],nums[i]
for i in range(len(nums)):
    if nums[i]!=i+1:
        print(i+1)
        break
else:
    print(len(nums)+1)