# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#this one is a fast and slow pointer problem
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # section 1 : find the middle of the list
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # section 2 : reverse the second half
        prev = slow 
        curr = slow.next
        slow.next = None
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        # section 3 : merge the two lists
        first, second = head, prev
        while first  and second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2

                
