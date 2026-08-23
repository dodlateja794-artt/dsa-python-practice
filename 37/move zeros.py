nums = [0,1,0,3,12]
answer=[]
for i in nums:
    if i!=0:
        answer.append(i)
zero_count=nums.count(0)
for i in range(zero_count):
    answer.append(0)
print(answer)