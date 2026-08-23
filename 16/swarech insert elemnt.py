arr=[1,3,5,6]
target=7
left=0
right=len(arr)-1
while left<=right:
    mid=(left+right)//2
    if mid==target:
        print(mid)
        break
    if arr[mid]>target:
        right=mid-1
    else:
        left=mid+1
print(left)