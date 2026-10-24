s = "({[]})"
pairs={
    ")":"(",
    "]":"[",
    "}":"{"
}
stack=[]
for ch in s:
    if ch in "([{":
        stack.append(ch)
    else:
        if not stack or stack[-1]!=pairs[ch]:
            print(False)
            break
        stack.pop()
if stack==[]:
    print(True)
else:
    print(False)