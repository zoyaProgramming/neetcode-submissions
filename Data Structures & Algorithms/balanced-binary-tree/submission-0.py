# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        mp = {None: 0}
        stack = [root]
        while len(stack) != 0:
            curr = stack[-1]
            if curr.left and curr.left not in mp: # can traverse left
                stack.append(curr.left)
            elif curr.right and curr.right not in mp:
                stack.append(curr.right)
            else:
                left_height = mp[curr.left]
                right_height = mp[curr.right]
                if abs(left_height - right_height) > 1:
                    return False
                else: 
                    curr = stack.pop()
                    mp[curr] = 1 + max(left_height, right_height)
        return True
    
