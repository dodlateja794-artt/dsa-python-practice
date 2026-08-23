nums = [1,2,3]
k = 3
prefix_sum=0
seen={}
window_sum=0
for i in nums:
    window_sum+=i
    if window_sum==k:
        if nums[i] in seen:
            count+=1
        else:
            count=1
print(count)
    

