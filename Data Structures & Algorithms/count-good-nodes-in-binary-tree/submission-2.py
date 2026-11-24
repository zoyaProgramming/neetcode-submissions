# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def goodNodes(self, root: TreeNode) -> int:
        paths = {root: root.val}
        stack = [root]
        count = 0
        while stack:
            node = stack.pop()
            val = max(node.val, paths[node])
            if val == node.val:
                count += 1
            if node.left:
                paths[node.left] = val
                stack.append(node.left)
            if node.right: 
                paths[node.right] = val
                stack.append(node.right)
        return count
