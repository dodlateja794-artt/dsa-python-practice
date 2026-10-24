def unique_path(rows,cols):
    dp=[[0]*cols for _ in range(rows)]
    for r in range(rows):
        dp[r][0]=1
    for c in range(cols):
        dp[0][c]=1
    for r in range(1,rows):
        for c in range(1,cols):
            dp[r][c]=dp[r-1][c]+dp[c][r-1]
    return dp[rows-1][cols-1]
print(unique_path(3,3))