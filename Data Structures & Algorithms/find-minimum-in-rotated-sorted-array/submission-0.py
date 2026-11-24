class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        res = -1
        while l < r:
            mid = (l + r)//2
            if nums[mid] > nums[r]: # in the large segment: right
                l = mid + 1
            else: # search left: 
                res = mid
                r = mid
        return nums[res]
                
