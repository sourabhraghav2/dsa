from dsa.model import ListNode

def listToLinkedList(arr):
    node=None
    head=None
    for i,value in enumerate(arr):
        if i==0: 
            node=ListNode(value,None)
            head=node
        else: 
            node.next=ListNode(value,None)
            node=node.next
    return head
