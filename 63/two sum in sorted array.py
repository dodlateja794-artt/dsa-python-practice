nums = [2, 3, 4, 7, 11, 15]
target = 9
left=0
right=len(nums)-1
while left<=right:
    sum=nums[left]+nums[right]
    if sum==target:
        print("found")
        break
    elif sum<target:
        left+=1
    else:
        right-=1



