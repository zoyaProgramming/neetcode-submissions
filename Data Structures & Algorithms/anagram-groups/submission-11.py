class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp2 =defaultdict(list)
        for s in strs: 
            tmp = [0 ] * 26 
            mp2["".join(sorted(s))].append(s)
                
        out = list(mp2.values())
        return out