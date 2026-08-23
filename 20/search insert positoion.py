arr=[1,2,4,5,6,8]
target=7
left=0
right=len(arr)-1
while left<=right:
    mid=(left+right)//2
    if arr[mid]<target:
        left=mid+1
    else:
        right=mid-1
print(left)