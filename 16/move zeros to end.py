arr=[1,2,0,3,0,4,3,0,2,800,2,45,0,0]
result=[]
for i in arr:
    if i !=0 :
        result.append(i)
zero_count=arr.count(0)
for i in range(zero_count):
    result.append(0)
print(result)