class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 0
        num = 0
        max = 0
        valid = lambda l, r : (r > l and r < len(prices) and l >= 0 and prices[l] >= prices[r])
        for end in range (0, len(prices)):
            if prices[end] - prices[left]   > max: 
                max =  prices[end] - prices[left]
            while valid(l=left, r=end):
                left = left + 1
        return max