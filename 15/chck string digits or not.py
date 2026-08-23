s="1234"
for i in s:
    if not i.isdigit():
        print("not digits")
        break
else:
    print("digits")
