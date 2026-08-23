matrix = [
 [1,3,5,7],
 [10,11,16,20],
 [23,30,34,60]
]
target = 3
rows=len(matrix)
cols=len(matrix[0])
left=0
right=rows*cols-1
while left<=right:
    mid=(left+right)//2
    
    row=mid//rows
    col=mid%rows
    value=matrix[row][col]
    if target==value:
        print(True)
        break
    elif target>value:
        left=mid+1
    else:
        right=mid-1
else:
    print(False)