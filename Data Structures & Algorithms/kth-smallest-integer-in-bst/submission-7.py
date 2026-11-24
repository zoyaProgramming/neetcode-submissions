# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        curr = root
        count = 0
        while curr is not None:
            if curr.left is None: # visit the node and go left
                count+= 1
                if count == k: return curr.val
                curr = curr.right
            else:
                # find the rightmost predecessor 
                prev = curr.left
                while prev.right is not None and prev.right != curr:
                    prev = prev.right
            
                if prev.right is None: # rightmost predecessor
                    prev.right = curr
                    curr = curr.left 
                else : # delete link
                    prev.right = None
                    count += 1
                    if count == k: return curr.val
                    curr = curr.right
        return -1

