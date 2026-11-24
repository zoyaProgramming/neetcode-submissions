# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorder(self, root):
        
        if not root: return [], 0
        left, left_l = self.inorder(root.left)
        left.append(root.val)
        right, right_l = self.inorder(root.right)
        left.extend(right)
        return left, left_l + right_l + 1
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root: return -1
        arr, l = self.inorder(root)
        print(arr)
        if k > l: return -1
        else: return arr[k-1]
        