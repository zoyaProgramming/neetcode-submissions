class Solution:
    def jump(self, nums: List[int]) -> int:
        # youre trying to 
        # dijikstra's algorithm ?
        # start from right? 
        # [0, 1, 0]
        idx = 0
        count = 0
        while idx < len(nums):
            print("looking at: ", idx)
            k = nums[idx]
            print("k : ", k)
            mx = idx + 1
            for i in range(idx + 1, min(idx + 1+ k, len(nums))):
                if i==len(nums) - 1:
                    return count + 1
                if i + nums[i] >= mx + nums[mx]: 
                    print("new max: ", nums[i])
                    mx = i

            count += 1
            idx = mx

        return count - 1