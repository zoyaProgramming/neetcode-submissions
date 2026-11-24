class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        maxf = 0
        res = 0
        if len(s) == 0: return 0
        counts: dict[str, int] = {
        }
        for i in range (0, len(s)):
            counts[s[i]] = 0
        for end in range(0, len(s)):
            counts[s[end]] = counts[s[end]] + 1

            maxf = max(maxf, counts[s[end]])
            window_size  = end - l 
            while end - l + 1  - maxf >  k:
                counts[s[l]] = counts[s[l]] - 1
                l = l + 1
            res = max(res, end - l + 1)
        return res 


        # left = 0
        # m = 0
        # if len(s) == 0: return 0
        # counts : dict[str, [int, int, int]] = {}
        # for i in range(0, len(s)):
        #     counts[s[i]] = [-1, k, -1]
        # prev = None
        # for end in range(0, len(s)):
        #     if counts[s[end]][0] == -1: 
        #         counts[s[end]][0]  = end
        #         counts[s[end]][2]  = end
        #     elif counts[s[end]][2] == end - 1:
        #         counts[s[end]][2] = end
        #     elif end - counts[s[end]][2] >= counts[s[end]][1]: 
        #         diff = end - counts[s[end]][2]
        #         counts[s[end]][1] = counts[s[end]][1] - diff
        #         counts[s[end]][2] = end
        #     else:
        #         left = 
        #     m = max(m, counts[s[end]][2] - counts[s[end]][0])
        #     print("Left: %d right: %d"%(counts[s[end] ][0], counts[s[end]][2]))
        # return m + 1
             
                 
            