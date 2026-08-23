intervals=[[1,3],[2,5],[7,11],[10,13]]
intervals.sort()
result=[]
for interval in intervals:
    if not result or interval[0]>result[-1][1]:
        result.append(interval)
    else:
        result[-1][1]=max(result[-1][1],interval[1])
print(result)

