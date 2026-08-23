arr=[1,2,3,99,4,23]
nums=set(arr)
max_length=0
for i in nums:
    if i-1 in nums:
        current=i
        length=1
        while current+1 in nums:
            current+=1
            length+=1
        max_length=max(length,max_length)
print(max_length)