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
        node = None
        while stack:
            node = stack.pop()
            if node.val >= paths[node]:
                count += 1
            if node.left:
                paths[node.left] = max(node.val, paths[node])
                stack.append(node.left)
            if node.right: 
                paths[node.right] = max(node.val, paths[node])
                stack.append(node.right)
        return count
