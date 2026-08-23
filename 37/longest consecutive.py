nums = [100,4,200,1,3,2]
seen=set(nums)
max_len=0
for i in nums:
    if i-1 not in seen:
        current=i
        length=1
        while current+1 in seen:
            current+=1
            length+=1
    max_len=max(max_len,length)
print(max_len)

            
            
            
            