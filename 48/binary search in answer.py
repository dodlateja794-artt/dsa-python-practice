weights = [1,2,3,4,5,6,7,8,9,10]
days = 5
left=1
right=max(weights)
while left<=right:
    mid=(left+right)//2
    if mid<days:
        left=mid+1
    else:
        right=mid-1
print(left)