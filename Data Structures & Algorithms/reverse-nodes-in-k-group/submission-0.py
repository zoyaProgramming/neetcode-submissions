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
            actual_prev = start 
            start = curr
            prev = curr
           
            
            
            tmp = curr
            print()
            for i in range(0, k ): 
              if tmp:
              
               tmp = tmp.next
                
              else: 
                print(curr.val)
                if actual_prev : actual_prev.next = prev
                return res 
            tmp = curr
            i = 1
            curr = curr.next
            prev.next = None
            while curr  and i < k :
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
                i += 1
            if actual_prev : actual_prev.next = prev

            if n_iters == 0:
                res = prev
               
            n_iters +=1 
        
        return res
            