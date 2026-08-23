nums = [100, 4, 200, 1, 3, 2]
arr=set(nums)
max_len=0
for i in arr:
    if i-1 not in arr:
        start=1
        length=1
        while start+1 in arr:
            start+=1
            length+=1
        max_len=max(max_len,length)
print(max_len)