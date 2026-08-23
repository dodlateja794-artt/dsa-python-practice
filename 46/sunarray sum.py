nums=[1,2,3,4,5]
k=3
prefix_sum=0
seen={}
count=0
for i in nums:
    prefix_sum+=i
    if (prefix_sum-k) in seen:
        count+=seen[prefix_sum-k]
