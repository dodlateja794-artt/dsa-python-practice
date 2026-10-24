arr = [100, 4, 200, 1, 3, 2]
set(arr)
max_len=0
for i in arr:
    if i-1 not in arr:
        current=i
        length=1
        while current+1 in arr:
            current+=1
            length+=1
        max_len=max(length,max_len)
print(max_len)