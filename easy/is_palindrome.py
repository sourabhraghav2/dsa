from typing import Optional
from dsa.model import ListNode
from dsa.util import listToLinkedList

def isPalindrome(head: Optional[ListNode]) -> bool:
    def reverse(node):
        prev=None
        current=node
        while current:
            temp_node=current.next
            current.next=prev
            prev,current=current,temp_node
        return prev
    slow=head
    fast=head
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
    
    comp1=head
    comp2=reverse(slow.next)
    while comp2:
        if comp1.val==comp2.val:
            comp1=comp1.next
            comp2=comp2.next
        else: return False
    return True

head=listToLinkedList([1,3,4,7,4,3,1])
print(isPalindrome(head))


