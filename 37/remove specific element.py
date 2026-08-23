a=[1,2,3,2,4,5]
remove=2
stack=[]
for i in a:
    if i!=remove:
        stack.append(i)
print(stack)