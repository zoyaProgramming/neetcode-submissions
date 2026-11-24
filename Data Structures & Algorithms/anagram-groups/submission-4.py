class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = defaultdict(lambda: [0] * 27)
        for s in strs:
            s = s.lower()
            if s not in mp:
                for c in s:
                    mp[s][ord(c) - ord('a')] += 1
       
        mp2 =defaultdict(list)
        out = []
        for s in strs:
            mp2[tuple(mp[s])].append(s) 
        for k in mp2:
            out.append(mp2[k]) 
        return out
