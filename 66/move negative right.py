nums = [3, -1, 4, -2, 0, -5, 6]
left=0
right=len(nums)-1
while left<right:
    if nums[left]<0:
        left+=1
    elif nums[right]>=0:
        right-=1
    else:
        nums[left],nums[right]=nums[right],nums[left]
        left+=1
        right-=1
print(nums)