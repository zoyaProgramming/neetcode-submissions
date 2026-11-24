class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast = 0 
        slow = 0
        # find the value at nums[duplicate number] bc. there's a cycle
        while True: 
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
            print(slow)     
        slow2 = 0
        while True:
            slow2 = nums[slow2]
            slow = nums[slow]
            if slow2 == slow:
                return slow
        return slow           
                
         