matrix = [
    [5, 9, 1],
    [7, 3, 8],
    [6, 4, 2]
]
largest=matrix[0][0]
for row in matrix:
    for num in row:
        if num>largest:
            largest=num
print(largest)