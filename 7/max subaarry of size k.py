arr=[1,1,3,4,1,3]
k=3
window_sum=sum(arr[:k])
max_sum=window_sum
for i in range(k,len(arr)):
    window_sum=window_sum+arr[i]-arr[i-k]
    max_sum=max(window_sum,max_sum)
print(max_sum)