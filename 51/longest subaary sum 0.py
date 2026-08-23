nums = [1, -1, 3, 2, -2, -3, 4]
seen={0:-1}
prefix_sum=0
max_length=0
for i in range(len(nums)):
    prefix_sum+=nums[i]
    if prefix_sum in seen:
        lenght=i-seen[prefix_sum]
        max_length=max(lenght,max_length)
    else:
        seen[prefix_sum]=i
print(max_length)
