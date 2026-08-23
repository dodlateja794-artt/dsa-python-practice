slow=head
fast=head
while fast and fast.next:
    slow=slow.next
    fast=slow.next.next
    if slow==fast:
        print(True)
else:
    print(False)