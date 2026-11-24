# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()
        q.append(root)
        res = []
        lvl = 1
        while q:
        
            first_counted= False
            for i in range (0, lvl):
                curr = q.popleft()
                lvl -= 1
                if curr:
                    q.append(curr.right)
                    q.append(curr.left)
                    lvl += 2
                    if not first_counted:
                        res.append(curr.val)
                        first_counted = True
        return res
           

                