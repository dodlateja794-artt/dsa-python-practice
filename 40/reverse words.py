s = "I Love Python"
result=[]
end=len(s)
for i in range(len(s)-1,-1,-1):
    if s[i]==" ":
        result.append(s[i+1:end])
        end=i
result.append(s[0:end])
print(result)


        
        