nums = [1, 1, 0, 1, 1, 1, 0, 1]
current=0
max_count=0
for i in nums:
    if i==1:
        current+=1
        max_count=max(current,max_count)
    else:
        current=0
print(max_count)