nums1 = [1, 2, 2, 3]
nums2 = [2, 2, 4]
seen=set(nums1)
result=[]
for i in nums2:
    if i in seen:
        result.append(i)
        seen.remove(i)
print(result)
