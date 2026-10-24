def product_sum(nums):
    result=[1]*len(nums)
    left=1
    for i in range(len(nums)):
        left*=nums[i]
        result[i]=left
    right=1
    for i in range(len(nums)-1,-1,-1):
        right*=nums[i]
        result[i]*=right
    return result
print(product_sum([1,2,3,4]))
