class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s ) == 0: return 0
        s_list = list(s)
        l = len(s)
        left = 0
        max_len = 1
        keys = {}
        for end in range(0, l):
        # increase right end
            while keys.get(s_list[end]) is not None:
                keys.pop(s_list[left])
                left = left + 1
            keys[s_list[end]] = 1
            max_len = max(max_len, end - left + 1)
        return max_len