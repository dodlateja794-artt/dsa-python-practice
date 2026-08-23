nums = [-1,0,1,2,-1,-4]
arr=sorted(nums)
for i in range(len(arr)):
    fixed=arr[i]
    left=i+1
    right=len(arr)-1
    while left<right:
        total=arr[i]+arr[left]+arr[right]
        if total==0:
            print(arr[i],arr[left],arr[right])
            left+=1
            right-=1
        elif total<0:
            left+=1
        else:
            right-=1
