import math
piles = [3,6,7,11]
h = 8
left=1
right=max(piles)
answer=-1
while left<=right:
    speed=(left+right)//2
    hours=0
    for pile in piles:
        hours+=math.ceil(pile/speed)
    if hours>h:
        left=speed+1
    elif hours<=h:
        answer=speed
        right=speed-1
print(answer)
