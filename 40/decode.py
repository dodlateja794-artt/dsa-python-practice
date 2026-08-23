s = "4#neet4#code4#love3#you"
result=[]
i=0
while i<len(s):
    j=i
    while s[j]!="#":
        j+=1
        length=int(s[i:j])
    start=j+1
    end=start+length
    word=s[start:end]
    result.append(word)
    i=end
print(result)

