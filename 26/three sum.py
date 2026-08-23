nums = [-2,0,1,1,2]
arr=sorted(nums)
for i in range(len(nums)):
    fixed=arr[i]
    left=i+1
    right=len(arr)-1
    while left<right:
        total=fixed+arr[left]+arr[right]
        if total==0:
            print(fixed,arr[left],arr[right])
            left+=1
            right-=1
        elif total<0:
            left+=1
        else:
            right-=1