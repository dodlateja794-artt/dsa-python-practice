import heapq
points = [[1,3], [-2,2]]
k = 1
heap=[]
for point in points:
    x=point[0]
    y=point[1]
    distance=x*x+y*y
    heapq.heappush(heap,(-distance,point))
    if len(heap)>k:
        heapq.heappop(heap)
result=[]
for item in heap:
    result.append(item[1])
print(result)
