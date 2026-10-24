nums = [1, 2, 3]
seen=set()
result=False
for i in nums:
    if i in seen:
        result=True
    else:
        seen.add(i)
print(result)


        



