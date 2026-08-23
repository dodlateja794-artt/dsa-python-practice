nums = [4,5,6,7,0,1,2]
target = 1
left=0
right=len(nums)-1
while left<=right:
    mid=(left+right)//2
    if nums[mid]==target:
        print(mid)
        break
    elif nums[left]<=nums[mid]:
        if nums[left]<=target<nums[mid]:
            right=mid-1
        else:
            left=mid+1
    else:
        if nums[mid]<target<=nums[right]:
            left=mid+1
        else:
            right=mid-1
