class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1, n2 = len(nums1), len(nums2)
        total = n1 + n2 
        if n2 < n1:
            nums1, nums2 = nums2, nums1
            n1, n2 = len(nums1), len(nums2)
        
        l, r = 0, n1-1
        half = total // 2 
        # find the pivot st. all elements are bigger than 
        # the middle value and 
        # that the number of items left of the middle value
        # is (n1 + n2 ) // 2
        while True:
            i = (l + r) // 2 # mid(A), i + 1 items 
            j = half - i - 2 # mid(numsB)

            Aleft = nums1[i] if i >= 0 else -math.inf   # 
            Aright = nums1[i + 1] if i + 1 < n1 else math.inf
            Bleft = nums2[j] if j >= 0 else  -math.inf
            Bright = nums2[j + 1] if j + 1 < n2 else math.inf
            # determine that all elements on the left side are smaller
            # The partitions are right
            if Aleft <= Bright and Bleft <= Aright:
                print(f"Aleft: {Aleft}, Bleft: {Bleft}, Aright: {Aright}, Bright: {Bright}, ")
                if (n1 + n2)%2 == 0:
                    return (max(Aleft, Bleft) + min(Aright, Bright))/2 
                else: 
                    return min(Aright, Bright)
            elif Bleft > Aright: #  B is too big
                l = i + 1
            elif Aleft > Bright:
                r = i - 1 
    



            
# 1, 3, 5,  6, 7 ,9 , 11
# 2 ,4, 10

# 11 = 5 elements on each side
# 3 on each side 


# 1, 2, 3,   4, 7,  9, 10
# 7 total : 3.5 elements
# something that has 3 on the left and 3 on the right
# 4: 4  < 7  and doesn't have so left is now 10




            

