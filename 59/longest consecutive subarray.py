arr = [1, 2, 1, 1, 1, 2, 3]
k = 3
prefix_sum=0
seen={0:-1}
max_len=0
for i in range(len(arr)):
    prefix_sum+=arr[i]
    if prefix_sum-k in seen:
        length=i-seen[prefix_sum-k]
        max_len=max(length,max_len)
    if prefix_sum not in seen:
            seen[prefix_sum] = i

print(max_len)
