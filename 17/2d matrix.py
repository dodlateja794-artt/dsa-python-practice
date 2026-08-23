matrix=[
    [1,2,3,4,5],
    [6,7,8,9,22],
    [11,12,13,14,15],
]
target=3
rows=len(matrix)
cols=len(matrix[0])
left=0
right=rows*cols-1
while left<=right:
    mid=(left+right)//2
    row=mid//cols
    col=mid%cols
    value=matrix[row][col]
    if value==target:
        print(True)
        break
    elif target>value:
        left=mid+1
    else:
        right=mid-1
else:
    print(False)