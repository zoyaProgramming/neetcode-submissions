# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []

        q = deque()
        q.append(root)
        d = {root: 0}
        res = [[]]
        while q:
            curr = q.popleft()
            lvl = d[curr]
            if lvl >= len(res): res.append([])
            if curr.left:
                d[curr.left] = lvl + 1
                q.append(curr.left)
            if curr.right:
                d[curr.right] = lvl + 1
                q.append(curr.right)
            res[lvl].append(curr.val)
        return res