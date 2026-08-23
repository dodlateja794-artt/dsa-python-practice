arr = [1, 2, 3, 1, 1, 1, 1]
k = 3
max_len=0
prefix_sum=0
seen={0:1}
for i in range(len(arr)):
    prefix_sum+=arr[i]
    if prefix_sum-k in seen:
        length=i-arr[i]
        max_len=max(length,max_len)
    else:
        seen.append(i)
print(max_len)

