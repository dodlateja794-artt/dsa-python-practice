nums = [1, 2, 1, 3, 4, 2, 3]
nums=sorted(nums)
max_len=0
for i in nums:
    if i-1 not in nums:
        current=i
        length=1
        while current+1 in nums:
            current+=1
            length+=1
        max_len=max(max_len,length)
print(max_len)