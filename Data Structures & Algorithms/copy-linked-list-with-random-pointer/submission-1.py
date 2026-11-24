"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None: return None
        randoms : dict[Node, int] = {}
        nodes  = []
        idx = 1

        prev = Node(head.val)
        nodes.append(prev)
        new_head = prev
        randoms[head] = 0
        old_head = head

        head = head.next
        while head is not None:
            randoms[head ] = idx
            curr = Node(head.val)
            nodes.append(curr)
            prev.next =  curr
            prev, head = curr, head.next
            idx = idx + 1
        head = old_head
        idx = 0
        prev = new_head
        while head is not None:
            if head.random:
                rand_idx = randoms[head.random] 
                prev.random = nodes[rand_idx]
            else:  head.random = None
            prev = prev.next
            head = head.next
        return new_head

        nodes = []
        