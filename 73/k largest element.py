import heapq

nums = [3, 2, 1, 5, 6, 4]
k = 2

heap = []
for i in nums:
    heapq.heappush(heap,i)
    if len(heap)>k:
        heapq.heappop(heap)
print(heap[0])
