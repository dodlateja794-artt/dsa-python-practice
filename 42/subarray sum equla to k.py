nums = [1, 2, 3]
k = 3
prefix_sum=0
count=0
seen={0:1}
for i in nums:
    prefix_sum+=i
    if (prefix_sum-k) in seen:
        count+=seen[prefix_sum-k]
    seen[prefix_sum]=seen.get(prefix_sum,0)+1
print(count)


