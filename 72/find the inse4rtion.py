nums = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
nums1=set(nums)
result=[]
for i in nums1:
    if i in nums2:
        result.append(i)
print(result)
