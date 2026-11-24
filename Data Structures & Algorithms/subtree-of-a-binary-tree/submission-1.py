# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    @staticmethod
    def serialize(root):
        if root is None: return "#", 0
        # use z - table (a table of longest common substring)
        s = ""
        stack = [root]
        count = 0
        while stack:
            top = stack.pop()
            s = s + "#" +  (str(top.val) if top is not None else "_")
            if top:
                s = s + "#" +  str(top.val)
                stack.append(top.right) 
                stack.append(top.left)
            else:
                s += "#_"
          
        print(s)
        return s, count

    def z_function(self, s: str) -> list:
        z = [0] * len(s)
        l, r = 0,0
        n = len(s)
        for i in range (1, len(s)):
            # case 1: i is within substring-box, so z[i] is computed 
            # in the prefix
            if i <= r:
                k = i - l
                z[i] = min(z[k], r - i + 1) # get the longest prefix
            # expand the  window while valid
            while i + z[i] < n and s[z[i]] == s[i + z[i]]:
                z[i] += 1
            # set the new valid window to the  old
            if i + z[i] - 1 > r:
                l, r = i, i + z[i] - 1
        return z
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot is None: return True
        root_str, root_l = self.serialize(root)
        pfx, pfx_l  = self.serialize(subRoot)
        l = len(pfx)
        # main loop
        if root_l < pfx_l : return False
        combined = pfx + "|" + root_str
    
        # for every z-value
        z = self.z_function(combined)
       
        for i in range(l + 1, len(combined) ):
            if z[i] == l:
                print(combined[i:])
                return True
        return False
                
            

        
        
        
        
                