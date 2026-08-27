intervals = [[1,3],[2,6],[8,10],[9,12]]
result=[]
for interval in intervals:
    if not result or interval[0]>result[-1][1]:
        result.append(interval)
    else:
        result[-1][1]=max(interval[1],result[-1][1])
print(result)