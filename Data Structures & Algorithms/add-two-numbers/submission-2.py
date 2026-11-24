# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def reverse (head: ListNode):
    if head is None : return None
    prev = head
    h1 = head.next
    prev.next = None
    while h1 is not None :
        h1.next, prev, h1 = prev, h1, h1.next
    return prev
class Solution:

    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None: return l2
        if l2 is None: return l1

        h1 = l1
        h2 = l2
        
        len1 = 1
        # len2 = 1
        print(h1.val)
        print(h2.val)
        # while h1 is not None and h1.next is not None and h2 is not None and h2.next is not None:
        #     h1.next, h1 = h1, h1.next 
        #     h2.next, h2 = h2, h2.next 
        #     len1, len2 = len1+1, len2 + 1
        # while h1 is not None and h1.next is not None:
        #     h1.next, h1 = h1, h1.next 
        #     len1 += 1
        # while h2 is not None and h2.next is not None:
        #     h2.next, h2 = h2, h2.next
        #     len2 += 1 
        # algorithm start : reversed
        carry = 0

        l3 = None
    
        # sum = h1.val + h2.val
        # l3 =  Node(h1.val + h2.val)
        # # if sum >= 10:
        # #     carry = sum/10
        print("dpne")
        sum = h1.val + h2.val
        if sum >= 10 : 
            carry = int(sum/10)
        l3 = ListNode(sum%10)
        hd = l3
        h1, h2 = h1.next, h2.next
        while h1 is not None and h2 is not None:
            
            sum = h1.val + h2.val + carry
            carry = 0
            if sum >= 10:
                carry = int(sum/10)
            new_val = ListNode(sum%10)
            # new_val.next = l3
            l3.next = new_val
            l3 = new_val
            print("Adding %d to right end " %(sum%10))
            h1 = h1.next
            h2 = h2.next
        
        while h1 is not None:
            print("not none")
            sum = h1.val + carry
            
    
            carry = 0
            if sum >= 10:
                carry = int(sum/10)
            new_val = ListNode(sum%10)
            l3.next = new_val
            l3 = new_val
            h1 = h1.next
        while h2 is not None:
            print("2 not none")
            sum = h2.val + carry
            carry = 0

            if sum >= 10:
                carry = int(sum/10)
            new_val = ListNode(sum%10)

            l3.next = new_val
            l3 = new_val
            h2 = h2.next
        if carry != 0: 
            print("c none")
            new_val = ListNode(carry)
            l3.next = new_val
            
        return hd

    