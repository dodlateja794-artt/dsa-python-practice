nums = [100, 4, 200, 1, 3, 2]
nums=set(nums)
max_len=0
for i in nums:
    if i-1 not in nums:
        current=i
        length=1
        while current+1 in nums:
            current+=1
            length+=1
        max_len=max(length,max_len)
print(max_len)