import math
piles=[3,5,7,11]
h=8
left=1
right=max(piles)

while left<=right:
    hours=0
    for pile in piles:
        mid=(left+right)//2
        hours+=math.ceil(pile/mid)
    if hours<=h:
        right=mid-1
    else:
        left=mid+1
print(left)