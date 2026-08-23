students = [10, 20, 10, 30, 20, 40]
seen=[]
for i in students:
    if i not in seen:
        seen.append(i)
print(seen)