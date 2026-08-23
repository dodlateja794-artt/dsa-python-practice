nums = [100,4,200,1,3,2]
arr=set(nums)
max_length=0
for i in nums:
    if i-1 not in arr:
        current=i
        length=1
        while current+1 in arr:
            current+=1
            length+=1
        max_length=max(length,max_length)
print(max_length)
