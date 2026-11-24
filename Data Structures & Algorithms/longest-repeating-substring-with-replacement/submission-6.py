class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        len_s = len(s)
        freq = {}
    
        most_freq = 0
        m = 0
        res = 0
        
        for r in range(0, len_s):
            
            freq[s[r]] = freq.get(s[r], 0) + 1
            
            most_freq =  max(most_freq, freq[s[r]])

            num_counted = r - l
            while r - l + 1 - most_freq > k:
                freq[s[l]] = freq[s[l]] - 1
                l = l + 1
            res = max(res,  r - l + 1)
            
        return res
