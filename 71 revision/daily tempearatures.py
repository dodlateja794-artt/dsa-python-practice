def daily_temps(temps):
    result=[-1]*len(temps)
    stack=[]
    for i in range(len(temps)):
        while stack and temps[stack[-1]]<temps[i]:
            index=stack.pop()
            result[index]=i-index
        stack.append(i)
    return result
print(daily_temps([73, 74, 75, 71, 69, 72, 76, 73]))