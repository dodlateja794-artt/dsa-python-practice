def houserobber(nums):
    if len(nums)<=2:
        return max(nums)
    prev2=nums[0]
    prev1=max(nums[0],nums[1])
    for i in range(2,len(nums)):
        current=max(prev1,nums[i]+prev2)
        prev2=prev1
        prev1=current
    return prev1
print(houserobber([2,7,9,3,1]))

