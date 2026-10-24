s = "({[]})"
pairs={
    "}":"{",
    "]":"[",
    ")":"("
}
stack=[]
result=True
for ch in s:
    if ch in "([{":
        stack.append(ch)
    else:
        if not stack or stack[-1]!=pairs[ch]:
            result=False
            break
        stack.pop()
if stack==[]:
    result=True
else:
    result=False
print(result)