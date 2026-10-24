nums = [4, 5, 0, -2, -3, 1]
k = 5
prefix_sum=0
seen={0:1}
count=0
for i in nums:
    prefix_sum+=i
    if prefix_sum%k in seen:
        count+=seen[prefix_sum%k]
    seen[prefix_sum%k]=seen.get(prefix_sum%k,0)+1
print(count)