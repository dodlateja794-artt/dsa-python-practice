nums = [1,1,2,2,3,3,4]
result=[]
for i in nums:
    if i not in result:
        result.append(i)
print(result)