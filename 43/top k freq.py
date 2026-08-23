import heapq
nums = [1,1,1,2,2,3]
k = 2
seen={}
heap=[]
for i in nums:
    if i in seen:
        seen[i]+=1
    else:
        seen[i]=1
for key,value in seen.items():
    heapq.heappush(heap,(-value,key))
result=[]
for _ in range(k):
    frequency,number=heapq.heappop(heap)
    result.append(number)
print(result)

    