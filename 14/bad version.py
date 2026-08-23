arr=[1,2,3,4,5]
bad=2
left=0
right=len(arr)-1
answer=-1
while left<=right:
    mid=(left+right)//2
    if arr[mid]>=bad:
       answer=arr[mid]
       right=mid-1
    else:
        left=mid+1
print(answer)