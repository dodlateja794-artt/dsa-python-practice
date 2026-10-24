def climb_stairs(n):
    if n<=2:
        return n
    prev2=1
    prev1=2
    for step in range(3,n+1):
        current=prev2+prev1
        prev2=prev1
        prev1=current
    return prev1
print(climb_stairs(5))