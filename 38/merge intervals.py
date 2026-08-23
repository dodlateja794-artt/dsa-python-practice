intervals = [[1,4],[2,5],[7,9],[8,10]]
intervals.sort()
result=[]
for interval in intervals:
    if not result or interval[0]>result[-1][1]:
        result.append(interval)
    else:
        result[-1][1]=max(interval[1],result[-1][1])
print(result)
