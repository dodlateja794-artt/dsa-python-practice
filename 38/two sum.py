nums = [3,2,4]
target = 6
seen={}
for i in range(len(nums)):
    diff=target-nums[i]
    if diff in seen:
        print(seen[diff],i)
    seen[nums[i]]=i