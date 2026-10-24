def greater_ele(nums):
    stack=[]
    result=[-1]*len(nums)
    for i in range(len(nums)):
        while stack and stack[-1]<nums[i]:
            index=stack.pop()
            result[index]=nums[i]
        stack.append(i)
    return result
print(greater_ele([4, 5, 2, 10, 8]))
        