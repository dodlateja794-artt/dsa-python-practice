arr=[1,3,2,5,-4,-3]
window_sum=arr[0]
max_sum=window_sum
for i in range(1,len(arr)):
    window_sum=max(arr[i],window_sum+arr[i])
    max_sum=max(window_sum,max_sum)
print(max_sum)