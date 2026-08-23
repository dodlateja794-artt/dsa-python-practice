heights = [1,8,6,2,5,4,8,3,7]
left=0
right=len(heights)-1
max_area=0
while left<right:
    width=right-left
    area=width*min(heights[left],heights[right])
    if heights[left]<heights[right]:
        left+=1
    else:
        right-=1
    max_area=max(area,max_area)
print(max_area)

