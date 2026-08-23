arr=[1,2,3,4,5]
found=7
for i in arr:
    if found in arr:
        print(True)
        break
    else:
        print(False)