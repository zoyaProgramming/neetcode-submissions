class Solution:
   # DEQUE approach
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = [0] * (len(nums) - k + 1)
        l,r = 0,0
        n = len(nums)
        mx = 0
        q = deque()
        i = 0
        while r  < n:
            curr = nums[r]
            # remove all the ones that are smaller than curr
            while q and nums[q[-1]] < curr:
                q.pop()
            # add curr to the queue
            q.append(r)
            
           
            if r - l + 1 < k: # increase
                r = r + 1
            else:   # valid
                res[i] = nums[q[0]]
                if  l == q[0]: q.popleft()
                l, r, i = l + 1, r + 1, i + 1 
        return res


                


                

