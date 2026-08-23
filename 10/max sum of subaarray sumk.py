arr = [1,4,2,1,5,3,1,0,20]
k = 4
window_sum=sum(arr[:k])
max_sum=window_sum
for i in range(k,len(arr)):
    window_sum+=arr[i]-arr[i-k]
    max_sum=max(window_sum,max_sum)
print(max_sum)