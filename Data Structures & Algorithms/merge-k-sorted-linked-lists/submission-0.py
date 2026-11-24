# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        my_head = ListNode()
        curr = my_head
        cnt = 0
        while cnt < len(lists):
            min_idx = 0
            for l in range(0, len(lists)): 
                if  lists[l] and (not lists[min_idx] or lists[l].val <= lists[min_idx].val):
                    min_idx = l
            if lists[min_idx]: 
                curr.next = ListNode(lists[min_idx].val)
                curr = curr.next
                lists[min_idx] = lists[min_idx].next
            else: 
                return my_head.next
                
                