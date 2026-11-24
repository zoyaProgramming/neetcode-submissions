
class WordDictionary:

    def __init__(self, root=None):
        self.root = root or {}
        
        

    def addWord(self, word: str) -> None:
        curr = self.root
       
        for i in range(0, len(word)):
            if word[i] not in curr:
                curr.update({word[i]: {}})
                curr = curr[word[i]]
            else:
                curr = curr[word[i]]
        curr[None] = {}
       
    def search(self, word: str) -> bool:
        print("searching ", word)
        curr = self.root
        prev = None
        i = 0
        l = len(word)
        while i < len(word):
            if word[i] != ".":
                if word[i] not in curr:
                    return False
                curr = curr[word[i]]
            else:
                for w in curr: # all letters
                    copy = curr[w]
                    print(copy)
                    if WordDictionary(copy).search(word[i+1: len(word)]): return True
                print(f"i: {i}, l-1: {l-1}")
                if None not in curr or i < l: return False
            i += 1
        if None in curr: return True
        return False
            
