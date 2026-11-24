# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
       
        stack = []
        curr = root
        count = 0
        while stack or curr:
            # push all of the leftmost onto the stack
            while curr:
                # print(curr.val)
                stack.append(curr)
                curr = curr.left
            
            curr = stack.pop()
            count = count + 1
            if count == k:  return curr.val

            curr = curr.right
            
            if count == k:  return curr.val
        return -1
            
