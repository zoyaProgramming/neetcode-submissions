class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n1, n2 = len(s), len(t)
        c_count = {None: 0}
        count_valid = 0
        mx = math.inf
        st = ""
        l,r=0,0
        for r in t:
            c_count[r] = c_count.get(r, 0) + 1
        for r in range(0, n1):
            #valid
            if s[r] in c_count: 
                c_count[s[r]] -= 1
                if c_count[s[r]] >= 0: count_valid += 1
                

            while r - l + 1 >= n2 and (s[l] not in c_count or c_count[s[l]] < 0):
                if s[l]  in c_count:
                    c_count[s[l]] += 1      
                l = l + 1
            
            if count_valid == n2 and r-l+1 < mx:
                st = s[l:r+1]
                mx = r-l+1 
        return st
            
