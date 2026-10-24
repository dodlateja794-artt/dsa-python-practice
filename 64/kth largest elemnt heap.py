import heapq
nums = [3, 2, 1, 5, 6, 4]
k = 2
heap=[]
for i in range(len(nums)):
    heapq.heappush(heap,nums[i])
    if len(heap)>k:
        heapq.heappop(heap)
print(heap[0])