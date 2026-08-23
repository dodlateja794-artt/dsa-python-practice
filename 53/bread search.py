from collections import deque
queue=deque([root])
result=[]
while queue:
    level=[]
    size=len(queue)
    for i in range(size):
        node=queue.popleft()
        