# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root: return False
        stack = [(root, lambda x: True, lambda y: True)]
        while stack:
            curr, leftp, rightp = stack.pop()
            if curr.left and (curr.left.val >= curr.val or not rightp(curr.left.val)) :
                return False
            elif curr.right and (curr.right.val <= curr.val or not leftp(curr.right.val)):
                return False
            val = curr.val
            if curr.left:
                d = lambda x , val=val: x < val
                stack.append((curr.left,  d, rightp))
            if curr.right: 
                d = lambda x , val=val: x > val
                stack.append((curr.right, leftp, d))
        return True

