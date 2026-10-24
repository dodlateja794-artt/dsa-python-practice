def three_sum(arr,target):
    nums=sorted(arr)
    result=[]
    for i in range(len(nums)):
        left=i+1
        right=len(nums)-1
        while left<right:
            total=nums[i]+nums[left]+nums[right]
            if total==target:
                result.append([nums[i],nums[left],nums[right]])
                left+=1
                right-=1
                break
            elif total<target:
                left+=1
            else:
                right-=1
    return result

print(three_sum([-4, -1, -1, 0, 1, 2],0))
