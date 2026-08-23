nums = [100,4,200,1,3,2]
seen=set(nums)
max_len=0
for i in nums:
    if i-1 not in seen:
        length=1
        current=i
        while current+1 in nums:
            length+=1
            current+=1
    max_len=max(max_len,length)
print(max_len)