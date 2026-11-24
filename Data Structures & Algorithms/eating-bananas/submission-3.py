class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # binary search
        

        # while l < r
            # mid = (l + r)/2
            # for pile in piles:
               
            #    if condition:
            #.      return rate
            #    elif condition < : 
            #.   else 
        
        
        r = max(piles)
        l = 1

        res = r
        while l <= r:
            mid = (l + r)//2
            s = 0           # num hours
            
            for pile in piles:
                if mid == 0:
                    s += 1
                elif pile%mid == 0:
                    s += int(pile/mid)
                else:
                    s += int(pile/mid) + 1
            if s <=  h:
                print("case 1 l: %d r : %d"%(l, r))
                res = mid
                r = mid - 1
            elif s > h: # takes too much time: shrink # hours
                print("case 2 l: %d r : %d s : %d"%(l, r, s))
                l = mid  + 1 
        return res
        
        
                
                

                
                
                