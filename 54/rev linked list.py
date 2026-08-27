prev=None
curr=head
while curr:
    next_node=curr.next  #save
    curr.next=prev   #reverse
    prev=curr   #move prev
    curr=next_node   #move curr
return prev
