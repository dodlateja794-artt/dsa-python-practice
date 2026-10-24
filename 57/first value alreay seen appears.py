nums = [2, 1, 3, 5, 3, 2]
seen=set()
for i in nums:
    if i in seen:
        print(i)
        break
    else:
        seen.add(i)