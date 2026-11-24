class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s ) == 0: return 0
        s_list = list(s)
        
        left = 0
        max_len = 1
        keys = {}
        for end in range(0, len(s_list)):
        # increase right end
            while keys.get(s_list[end]) is not None:
                print("left : %c  end : %c idx %d" % (s_list[left], s_list[end], end) , s_list[end])
                
                print("popping %c, dict: %s"% (s_list[left], str(keys)))
                keys.pop(s_list[left])
                left = left + 1
            keys[s_list[end]] = 1
            print("adding %c"%(s_list[end]))
            max_len = max(max_len, end - left + 1)
        return max_len