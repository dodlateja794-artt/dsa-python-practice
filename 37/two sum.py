nums = [2,7,11,15]
target = 9
seen={}
for i in range(len(nums)):
    diff=target-nums[i]
    if diff in seen:
        print(seen[diff],i)
    seen[nums[i]]=i