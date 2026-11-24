class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]: 
        mp2 =defaultdict(list)
        for s in strs:
            s = s.lower()
            tmp = [0 ] * 26
            for c in s:
                tmp[ord(c) - ord('a')] += 1
            mp2[tuple(tmp)].append(s)
                
        out = []
        for k in mp2:
            out.append(mp2[k]) 
        return out
