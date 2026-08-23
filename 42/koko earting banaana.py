import math
piles=[3,5,7,11]
h=8
left=1
right=max(piles)
while left<=right:
    total_hours=0
    mid=(left+right)//2
    for pile in piles:
        total_hours+=math.ceil(pile/mid)
    if total_hours<=h:
        right=mid-1
    else:
        left=mid+1
print(left)
