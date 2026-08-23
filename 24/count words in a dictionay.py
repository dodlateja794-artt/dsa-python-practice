words = ["python", "java", "python", "sql", "java", "python"]
seen={}
for word in words:
    if word in seen:
        seen[word]+=1
    else:
        seen[word]=1
print(seen)
