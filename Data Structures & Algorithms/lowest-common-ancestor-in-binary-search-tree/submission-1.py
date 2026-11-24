# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root.left == p or root.right == q or root.left == q or root.right ==p: # diverging
            return root
        elif p.val > root.val and q.val > root.val: # return 
            return self.lowestCommonAncestor(root.right, p, q)
        elif p.val < root.val and q.val < root.val: # go deeper on the left tree
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root
  #             6
   #         2     8
   #       0  4  7 9 
   #         3 5
    
        # left = self.lowestCommonAncestor( root.left, p, q)
        # right = self.lowestCommonAncestor(root.right, p, q)

        # elif p.val < root.val and q.val < root.val:
        #     return lowestCommonAncestor(root.left, p, q)
        