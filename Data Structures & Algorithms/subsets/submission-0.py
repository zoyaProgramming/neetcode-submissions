class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        my_set=set([frozenset(nums)])
        res = [nums]
        for num in nums:
            my_lst = []
            for s in my_set:
                print(s)
                n = frozenset(s - set([num]))
                my_lst.append(frozenset(s - set([num])))
                res.append(list(n))
            my_set.update(my_lst)
           # res.append(list(my_lst))
            
        return res