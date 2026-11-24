# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        q = deque([(root, 0, 0)])
    
        lst = []
        max_lvl = -1
        if not root: # '#' for the end of a node
            return "#"
        else:
            while q:
                curr, lvl, idx = q.popleft()
                if curr:
                    #if lvl > max_lvl: # need to extend list
                    #    lst.extend(["#0$"] * pow(2, lvl))
                    lst.append(f"{curr.val}#{idx}$")
                    q.append((curr.left, lvl + 1, idx * 2 + 1))
                    q.append((curr.right, lvl + 1, idx * 2 + 2))
            return "".join(lst)
            

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "": return None
        print(data)
        pat = re.compile(r"(-?\d*)#(\d+)\$")
        lst = []
        root = TreeNode(0)
        q = deque([(0, 'r')])
    
        s = ""
        start, end = 0, len(data)
        d = {}
        print(root.right)
        while match := pat.match(data, start):
            if match.end(0) == start:
                # nothing found
                return None
            else:
                start = match.end(0) 
            
            if match.end(1) != match.start(1): 
                n = TreeNode(int(match.group(1)))
            else: 
                n = None

            index = int(match.group(2))
            d[index] = n
            parent_index = (index - 1)//2 
            print(f"parent index: {parent_index} actual val: {n.val}" )
          #  q.append((index * 2 + 1, 'l'))
       #     q.append((index * 2 + 2, 'r'))
           # if parent_index == -1 :
            if parent_index == -1:
                root.right = n
            if parent_index > 0 and (parent_index not in d or not d[parent_index] and n):
                print(parent_index)
                print("parent is null but the current node is not null")
                return None
            elif parent_index in d and d[parent_index]:
                parent = d[parent_index]
                if parent and parent_index*2 + 1 == index:
                    print(f"{n.val if n else None} left of {parent.val}")
                    parent.left = n
                else:
                    print(f"{n.val if n else None} right of {parent.val}")
                    parent.right = n
        print(root.val)
        print(root.right)
        return root.right

            



