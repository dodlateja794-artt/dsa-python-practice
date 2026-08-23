s="4#teja4#balu3#sri5#durga"
i=0
result=[]
while i<len(s):
    j=i
    while s[j]!="#":
        j+=1
    length=int(s[i:j])
    start=j+1
    end=start+length
    word=s[start:end]
    i=end
    result.append(word)
print(result)
