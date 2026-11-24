def get_idx(c):
    return ord(c) - ord('a')
class TrieNode:
    value: str
    def __init__(self, idx=-1):
        self.children = [None] * 26
        self.idx = idx
        self.num_childs = 0
        self.is_word = False
        
    def add_word(self, word):
        word = word.lower()
        curr = self
        for i in range(0, len(word)):
            if not curr.children[get_idx(word[i])]:
                curr.children[get_idx(word[i])] = TrieNode()
                curr = curr.children[get_idx(word[i])]
            else:
                curr = curr.children[get_idx(word[i])]
        curr.is_word = True
    def __str__(self):
        curr = self 
        lst = []
       
        def rec_str(base, st): 
            nonlocal lst
            
            if not st:
                return base
            if st.is_word:
                lst.append(base)
            if st.children is not None:
                for i in range(0, 26):
                    child = chr(ord('a') + i)
                    if st.children[i]: (rec_str(base + child, st.children[i]))
        
        rec_str("", self)
        return ", ".join(lst)

class Solution:

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        h,w = len(board), len(board[0])
        lst = []
        for word in words:
            root.add_word(word)

        def get_idx(c):
            return ord(c) - ord('a')
        
        def dfs(node, row, col, wd =""):
            nonlocal lst, board
            if (row >= h or col >= w
            or row < 0 or col < 0
            or board[row][col] == "*" 
            or not node.children[get_idx(board[row][col])] ):
                # if invalid idx or the current char isn't 
                # part of valid word
                return None
            tmp = board[row][col]
            node = node.children[get_idx(board[row][col])]
            wd += tmp
            board[row][col] = "*"
            if node.is_word and node.idx == -1: 
                # print("Found it !! ")
                # print(wd)
                lst.append(wd)
                node.idx = len(lst) - 1
            
            dfs(node, row, col-1, wd)
            dfs(node, row, col+1, wd)
            dfs(node, row-1, col, wd)
            dfs(node, row+1, col, wd)
            board[row][col] = tmp
        for row in range(0, h):
            for col in range(0,w):
                dfs(root, row, col)
        return lst
        