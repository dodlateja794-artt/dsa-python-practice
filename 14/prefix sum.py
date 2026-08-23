arr = [5,2,1,3]
prefix_sum=0
result=[]
for i in range(len(arr)):
    prefix_sum+=arr[i]
    result.append(prefix_sum)
print(result)