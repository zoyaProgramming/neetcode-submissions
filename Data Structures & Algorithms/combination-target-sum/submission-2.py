
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # approach - use sets
        # get all common subsets
        lst = []
        nums.sort()
        out = set()
        def dfs(total, arr, i):
            if total == target :         
                lst.append(arr.copy())
                return
        
            
            for j in range( i, len(nums)):
                if total + nums[j] > target: 
                    return 
                arr.append(nums[j])
                dfs(total + nums[j], arr, j)
                arr.pop()
                  
        dfs(0, [], 0)
        
        return lst