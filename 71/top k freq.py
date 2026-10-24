import heapq
def heap(nums):
    count={}
    for i in nums:
        count[i]=count.get(i,0)+1
    heap=[]
    k=2
    for key,value in count.items():
        heapq.heappush(heap,(value,key))
        if len(heap)>k:
            heapq.heappop(heap)
    result=[]
    for value,key in heap:
        result.append(key)
    return result
print(heap([1,1,1,2,2,3]))