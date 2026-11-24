# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        head = TreeNode(None)
        curr = head
        i, j, n = 0, 0, len(preorder)

        while i < n and j < n:
            # create new Node in between curr and right
            curr.right = TreeNode(preorder[i], left=None, right=curr.right)
            curr = curr.right
            i += 1

            # leftmost predecessor ??
          
            print(f"i:%d j%d", i , j)
            while i < n and curr and curr.val != inorder[j]:
                curr.left = TreeNode(preorder[i], right=curr)
                curr = curr.left
                i += 1

            # find the right
            j += 1
            while j < n and curr.right and inorder[j] == curr.right.val:
                temp = curr.right
                curr.right = None
                curr = temp
                j += 1
        return head.right



# walk thru
# iteration 1: curr.right = Treenode(1, right = None)
#   1.left = 2, links back to 1
#.  i is now 2, j is 0
#  