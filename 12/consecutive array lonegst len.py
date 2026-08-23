arr=[1,2,3,500,50]
max_len=0
for i in range(len(arr)):
    if i-1 not in arr:
        current=i
        length=1
        while current+1 in arr:
            current+=1
            length+=1
    max_len=max(max_len,length)
print(max_len)