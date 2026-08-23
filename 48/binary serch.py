nums = [1, 2, 2, 2, 3, 4, 5]
target = 2
left=0
right=len(nums)-1
while left<right:
    mid=(left+right)//2
    if nums[mid]==target:
        answer=mid
        right=mid-1
        break
    elif nums[mid]>=target:
        right=mid-1
    else:
        left=mid+1
print(mid)
