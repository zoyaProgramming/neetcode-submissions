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
        while stack or curr:
            # append the left nodes to the top of the stack
            while curr:
                stack.append(curr)
                curr = curr.left
            # get the top node
            curr = stack.pop()
            print(curr.val)
            k -= 1

               
            if k==0: return curr.val

            curr = curr.right

