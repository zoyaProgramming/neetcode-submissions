# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        len = 0
        fast = head 
        slow = head
        prev = None
        #slow reaches the halfway point
        while fast is not None and fast.next is not None:
            len = len + 2
            fast=fast.next.next
            prev = slow
            slow=slow.next
        if fast is not None: # odd length
            len = len + 1
        # should be behind
        half_len = 0
        
        slow = head
        prev = None
        while half_len < len -  n:
            prev = slow
            print(prev)
            slow = slow.next
            half_len = half_len + 1
        if prev is not None: 
            prev.next = slow.next
        elif slow is not None:
            head = slow.next
        else :
            head = None
        return head
