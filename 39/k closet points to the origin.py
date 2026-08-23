import heapq
points = [[1,3],[-2,2],[5,8]]
heap=[]
for point in points:
    distance=point[0]**2+point[1]**2
    heapq.heappush(heap,(distance,point))
result=[]
k=2
for _ in range(k):
    distance,point=heapq.heappop(heap)
    result.append(point)
print(result)