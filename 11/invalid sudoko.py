s=[1,2,3,2]
seen=[]
sudoko=True
for i in s:
    if i in seen:
        sudoko=False
        break
    seen.append(i)
print(sudoko)