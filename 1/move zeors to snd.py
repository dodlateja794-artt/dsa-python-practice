arr=[1,0,2,0,3,4,5,0]
result=[]
for i in arr:
    if i!=0:
        result.append(i)
zero_counnt=arr.count(0)
for i in range(zero_counnt):
    result.append(0)
print(result)