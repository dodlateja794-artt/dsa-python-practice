import heapq
strs=[[1,2],[-2,3],[4,5]]
k=2
heap=[]
for point in strs:
    distance=point[0]**2+point[1]**2
    heapq.heappush(heap,(distance,point))
result=[]
for _ in range(k):
    distance,point=heapq.heappop(heap)
    result.append(point)
print(result)


    
    
