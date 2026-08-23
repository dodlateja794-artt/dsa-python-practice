arr=[1,2,3,200,4]
nums=set(arr)
max_length=0
for num in nums:
    if num-1 not in nums:
        current=num
        length=1
        while current+1 in nums:
            current+=1
            length+=1
        max_length=max(max_length,length)
print(max_length)