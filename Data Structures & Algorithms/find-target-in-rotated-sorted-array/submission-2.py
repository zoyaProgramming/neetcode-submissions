class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) -1 
        while l <= r:
            mid = (l + r)//2
            if nums[mid] == target: return mid
            elif nums[mid] > nums[r]: # in the large segment
                if target <= nums[r]: # target is in the small segment
                    l = mid + 1
                elif target > nums[mid]: #target is right 
                    l = mid + 1
                else : 
                    r = mid - 1
            else: # in the small segment
                if target > nums[r]: # target is also > nums[mid]
                    r = mid - 1
                elif target > nums[mid]:
                    l = mid + 1
                else: 
                    r = mid - 1
        return -1

