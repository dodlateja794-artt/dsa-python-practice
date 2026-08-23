import math
piles = [3, 6, 7, 11]
h = 8
left=1
right=max(piles)

while left<=right:
    mid=(left+right)//2
    hours=0
    for pile in piles:
        hours+=math.ceil(pile/mid)
    if hours<=h:
        answer=mid
        right=mid-1
    else:
        left=mid+1
print(answer)

