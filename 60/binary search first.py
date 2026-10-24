arr = [1, 2, 2, 2, 4, 5, 7]
target = 2
left=0
right=len(arr)-1
while left<=right:
    mid=(left+right)//2
    if arr[mid]==target:
        answer=mid
        right=mid-1
    elif arr[mid]>target:
        right=mid-1
    else:
        left=mid+1
print(answer)