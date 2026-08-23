list1=[]
list2=[]
while fast and fast.next:
    slow=slow.next
    fast=fast.next.next
    if slow==fast:
        print(True)
    else:
        print(False)