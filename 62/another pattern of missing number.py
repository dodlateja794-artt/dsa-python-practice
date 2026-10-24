nums = [3, 0, 1]
result=0
for i in range(len(nums)+1):
    result=result^i
for num in nums:
    result=result^num
print(result)