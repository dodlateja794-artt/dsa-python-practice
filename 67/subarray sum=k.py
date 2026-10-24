nums = [1, 2, 3, -2, 5]
k = 5
prefix_sum=0
count=0
seen={0:1}
for i in nums:
    prefix_sum+=i
    req_prefix=prefix_sum-k
    if req_prefix in seen:
        count+=seen[req_prefix]
    seen[prefix_sum]=seen.get(prefix_sum,0)+1
print(count)

        