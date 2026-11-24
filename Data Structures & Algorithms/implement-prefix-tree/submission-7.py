class TreeNode :
    def __init__(self, value, left=None, right=None):
        self.left = left 
        self.right = right
        self.value = value
class PrefixTree:

    def __init__(self):
        self.root = {}


    def insert(self, word: str) -> None:
        if len(word ) == 0 : return
        curr = self.root
        for i in range (0, len(word)):
            if word[i] not in curr:
                curr[word[i]] = {}
            curr = curr[word[i]]
        curr['\n'] = {}

                
    def search(self, word: str) -> bool:
        if len(word) == 0: return False
        curr = self.root
        for i in range(0, len(word)):
            if word[i] not in curr:
                return False
            curr = curr[word[i]]
        if '\n' in curr: return True
        else: 
            print("?")
            print(word)
            print(self.root)
            return False

    def startsWith(self, prefix: str) -> bool:
        if len(prefix) == 0: 
            print("?")
            return False
        curr = self.root
        for i in range(0, len(prefix)):
            if prefix[i] not in curr:
                print(prefix)
                return False
            curr = curr[prefix[i]]
        return True
        
        