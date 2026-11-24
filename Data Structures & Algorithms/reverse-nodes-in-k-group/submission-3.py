# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        prev = None
        n_iters = 0
        res = None
        start = None
        while curr:
            prev_end = start  # end of the previous list
            start = curr
            # check if there are enough total nodes to reverse
            # the linked list
            prev = curr
            for i in range(0, k ): 

              if prev:
                prev = prev.next
              else: 
                if prev_end : prev_end.next = start
                return res 
            # reverse the linked list
            prev = start
            i = 1
            curr = curr.next
            prev.next = None
            while curr  and i < k :
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
                i += 1
            if prev_end : prev_end.next = prev
            if n_iters == 0:
                res = prev
            n_iters +=1 
        
        return res
            