import math
piles = [3, 6, 7, 11]
k = 6

left=1
right=max(piles)
while left<=right:
    total_hours=0
    mid=(left+right)//2
    for pile in piles:
        hours=math.ceil(pile/mid)
        total_hours+=hours
        if total_hours<=k:
            left=mid+1
        else:
            right=mid-1
        