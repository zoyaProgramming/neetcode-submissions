# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: return True
        elif not p or not q: return False
        s1 = [p]
        s2 = [q]
        while s1 and s2:
            node1, node2 = s1[-1], s2[-1]
            if not node1 and node2 or not node2 and node1:
                print("one")
                return False
            elif not node1 and not node2:
                s1.pop()
                s2.pop()
            elif   (node1.val == node2.val): 
                print("Node1: %d, Node2: %d"%(node1.val, node2.val))
                s1.pop()
                s2.pop()
                s1.append(node1.left)
                s1.append(node1.right)
                s2.append(node2.left)
                s2.append(node2.right)
            elif node1.val != node2.val:
                print("???")
                return False
            else:
                print("???")
                return False
        return True

                
            
                 