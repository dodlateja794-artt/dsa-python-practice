def subsets(nums):
    current=[]
    result=[]
    def backtrack(index):
        if index==len(nums):
            result.append(current.copy())
            return
        backtrack(index+1)
        current.append(nums[index])
        backtrack(index+1)
        current.pop()
    backtrack(0)
    return result
print(subsets([1,2,3]))
print(len(subsets([1,2,3])))