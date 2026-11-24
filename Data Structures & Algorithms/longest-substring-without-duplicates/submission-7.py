class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map : dict[str, int] = {s[i]:0 for i in range(len(s))}
        l = 0
        m = 0
        for r in range(0, len(s)):
            map[s[r]] += 1

            while map[s[r]] > 1:
                map[s[l]] -= 1
                l = l + 1
            
            m = max(m, r - l + 1)
        
        return m
        


        