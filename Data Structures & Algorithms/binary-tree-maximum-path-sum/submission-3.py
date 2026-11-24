# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        v : dict[TreeNode, int]= {root: 0}
        unvisited = [root]
        sums = []      # the weight to get to that node
        parents = []            # node that created the weight  
        curr = root
        # get the path sums from root
        def dfs(root, total, parent, idx):
            pass_to_parent = True
            if not root:
                print("empty root")
                v[root] -= 1
                return 0, False
            else: 
                print(f"entering {root.val}, total : {total}")

            idx_l = (idx * 2) + 1
            idx_r = (idx * 2) + 2
            indx_p = ((idx -1 ) // 2)
            f = False
            # cut off connection to parent 
            if total < 0 and total < root.val: 
                print("negative total")
                total = 0
                v[parent] -= 1
                v[root] -= 1
                pass_to_parent = False

            # add links to children
            v[root] += 2
            v.update({root.left: v.get(root.left, 0) + 1})
            v.update({root.right: v.get(root.right, 0) + 1})

            left, p1 = dfs(root.left, total + root.val, root,idx_l)
            left = left - (total + root.val)
            right, p2 = dfs(root.right, total + root.val, root,idx_r)
            right = right - (total + root.val)
            new_total = total + root.val
          
            if (left > 0 and p1) and (right > 0 and p2) and (v[root] == 3):
                # choose 1 branch to prevent loops
                print("case 1: must choose a branch to prevent a loop")
                v[root] -= 1
                if left < right:
                    v[root.left] -= 1
                else:
                    v[root.right] -= 1
                new_total += max(left, right)
            elif (left>0 and p1) and (right>0 and p2) and v[root] == 2:
                # valid setup 
                print("case 2: combine everything")
                new_total += left
                new_total += right
            elif p1 and p2:
                print("Case 3: both children are valid, but one of them might be negative ")
                # one of them is invalid
                if p1 and left > 0: 
                    new_total += left
                else: 
                    v[root.left] -= 1
                    v[root] -= 1
                if p2 and right > 0 : new_total += right
                else: 
                    v[root.right] -= 1
                    v[root] -= 1
            else:  
                print("case 4: one of either p1 or p2 is invalid")
                if p1 and left > 0: new_total += left
                elif left <= 0:
                    v[root.left] -= 1
                    v[root] -= 1
                if p2 and right > 0: new_total += right
                elif right <= 0:
                    v[root.right] -= 1
                    v[root] -= 1


                
            print(f"l: {left} right: {right} curr: {root.val} total: {total}, new: {new_total}")
            sums.append(new_total)
            return new_total, pass_to_parent
        dfs(root, 0, None,0)
        mx = -math.inf
        for i in range(0, len(sums)):
            if sums[i] > mx: mx = sums[i]
        return mx

#     5
#.  4    8 
# 11    13 4
#7 2.     1