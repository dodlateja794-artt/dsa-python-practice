import heapq
nums=[1,2,1,1,2,3]
k=2
heap=[]
seen={}
for i in nums:
    if i in seen:
        seen[i]+=1
    else:
        seen[i]=1
for key,value in seen.items():
    heap=heapq.heappush(heap,(-value,key))
result=[]
for _ in range(k):
    result.append(heapq.heappop(heap))
print(result)
    