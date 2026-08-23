arr = [-1, 0, 1, 2, -1, -4]
nums=sorted(arr)
result=[]
for i in range(len(nums)):
    left=i+1
    right=len(nums)-1
    
    while left<right:
        total=nums[i]+nums[left]+nums[right]
        if total==0:
            result.append([nums[i],nums[left],nums[right]])
            left+=1
            right-=1
            break
        elif total<0:
            left+=1
        else:
            right-=1
print(result)
