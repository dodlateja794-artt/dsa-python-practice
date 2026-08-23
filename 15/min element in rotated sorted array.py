arr=[1,0,2,3,4,5,7]
left=0
right=len(arr)-1
while left<right:
    mid=(left+right)//2
    if arr[mid]>arr[right]:
        left=mid+1
    else:
        right=mid
print(arr[left])