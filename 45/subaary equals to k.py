nums = [1, 2, 1, 2, 1]
k = 3
seen={0:1}
count=0
prefix_sum=0
for i in nums:
    prefix_sum+=i
    if (prefix_sum-k) in seen:
        count+=seen[prefix_sum-k]
    if prefix_sum in seen:
        seen[prefix_sum]+=1
    else:
        seen[prefix_sum]=1
print(count)