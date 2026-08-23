import math
piles=[3,5,7,11]
h=8
left=1
right=max(piles)
answer=[]
for pile in piles:
    mid=(left+right)//2
    hours+=math.ceil(pile/mid)
    if hours<=h:
        answer=mid
        right=mid+1
    else:
        left=mid-1
print(left)


