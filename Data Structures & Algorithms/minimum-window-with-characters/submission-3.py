class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        n = len(s)
        sz = math.inf
        res = ""
        count = {None: 0}
        num_rem = len(t)
        for r in t:
            count.update({r: count.get(r, 0) + 1})
        
        for r in range(0 , n):
            #update the array
            if s[r] in count:
                count.update({s[r]: count.get(s[r]) - 1})
                if count.get(s[r], -1) >= 0:
                    num_rem -= 1

            #shrink the array
            while l <= r - len(t) and (s[l] not in count or count[s[l]] < 0):
                if s[l] in count:
                    count.update({s[l]: count.get(s[l]) + 1})
                    if count[s[l]] > 0: num_rem += 1
                else:
                    count.update({None: count.get(None) - 1})
                l = l + 1

            # update variables
            new_sz = (r - l + 1 )
           
            if num_rem == 0:
                if sz > new_sz:
                    res = s[l:r + 1]
                    sz = new_sz
        return res
                

                
