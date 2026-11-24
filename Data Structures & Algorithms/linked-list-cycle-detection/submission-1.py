# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None: return False
        fastPtr, slowPtr = head.next,head
        while fastPtr is not None and fastPtr.next is not None:
            if fastPtr == slowPtr: return True
            fastPtr = fastPtr.next.next 
            slowPtr = slowPtr.next
        return False
        