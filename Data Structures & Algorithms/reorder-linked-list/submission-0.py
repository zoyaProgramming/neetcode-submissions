# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 2 lists
        if head == None or head.next == None or head.next.next == None :return
        l2 = head
        tl = head
        
        while tl is not None and tl.next is not None:
            tl = tl.next.next
            prev = l2
            l2 = l2.next
        
        prev.next= None
        print("prev : %d l2 : %d" %(prev.val, l2.val))
        prev2 = None
        
        while l2 is not None:
            l2.next, prev2, l2 = prev2, l2, l2.next
        l1 = head
        l2 = prev2
        curr = l1
        
        t = l1
        while t is not None:
            print("l1: " , t.val)
            t = t.next
        
        t = l2
        while t is not None:
            print("l2: " , t.val)
            t = t.next

        
        print("L1: %d L2 : %d" %(l1.val, l2.val))
        curr = l1
        prev = None
        while l1 is not None and l2 is not None:
        #      # 1. Save the next nodes for BOTH lists so we don't lose them
            next_l1 = l1.next
            next_l2 = l2.next
            
        # #     # 2. Link l1 to l2
            curr.next = l2
            curr = curr.next
            prev = curr
            curr.next = next_l1
            curr = curr.next
            
        #     # 3. Advance our main pointers to the saved next nodes
            l1 = next_l1
            l2 = next_l2
        print(prev.val)
        if l1 is not None:
            prev.next = l1
        elif l2 is not None:
            prev.next = l2


        

            

        
        

        


        