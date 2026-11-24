# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root: return False
        stack = [(root, -1 * math.inf, math.inf)]
        while stack:
            curr, left, right = stack.pop()
            if curr.left and (curr.left.val >= curr.val or not (curr.left.val >   left)) :
                print("left", left)
                return False
            elif curr.right and (curr.right.val <= curr.val or not (curr.right.val < right)):
                print("right", right ," curr ", curr.right.val)
                return False
            val = curr.val
            if curr.left:
                stack.append((curr.left,  left, val))
            if curr.right: 
                stack.append((curr.right, val, right))
        return True

