nums = [0, 1, 1, 0, 1, 0, 0, 1]
prefix_sum=0
lenght=0
seen={0:-1}
for i in range(len(nums)):
    if nums[i]==0:
        nums[i]=-1
for i in range(len(nums)):
    prefix_sum+=nums[i]
    if prefix_sum in seen:
        curr_lenght=i-seen[prefix_sum]
        lenght=max(lenght,curr_lenght)
    else:
        seen[prefix_sum]=i
print(lenght)