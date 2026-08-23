s="()[]"
stack=[]
pairs={
    ')':'(',
    ']':'[',
    '}':'{'
}
for ch in s:
    if ch in "([":
        stack.append(ch)
    else:
        if not stack or stack[-1]!=pairs[ch]:
            print("false")
            break
        stack.pop()
else:
    if stack==[]:
        print("true")
    else:
        print("false")


        