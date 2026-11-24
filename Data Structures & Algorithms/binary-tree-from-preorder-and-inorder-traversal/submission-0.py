# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# choose an inorder idx and add all the inorder  as left of the preorder until
# in idx is found in preorder

# ex : 
# 2, 4, 3 , 8 , 9, 10, 12
# 8, 4, 2
    
class Solution:
    
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        head = TreeNode(None)
        curr = head
        i, j = 0, 0
        n = len(preorder)
        while i < n and j < n:
            newNode = TreeNode(preorder[i], right=curr.right)
            curr.right = newNode
            curr = curr.right

            # look for predecessor
            i = i + 1
            while i < n and curr and curr.val != inorder[j]:
                curr.left = TreeNode(preorder[i], right=curr)
                curr = curr.left
                i+=1
            
            j = j + 1
            while curr.right and j < n  and curr.right.val == inorder[j]:
                temp = curr.right
                curr.right = None
                curr = temp
                j = j + 1
        return head.right


#     8
#    4.    10
#   2. 3 9     12
# inorder : 2, 4, 3, 8, 9, 10, 12
# preorder = 8, 4, 2, 3, 10, 9, 12

# 

#preorder:  1, 2, 3, 4
#inorder:  2, 1, 3, 4
            