class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # step 1. find the max number so u can make an array
        max_num = 0
        for start, end in intervals:
            max_num = max(end + 1, max_num )
        # step 2: 1 end per start of an .
        mp = [0]  * max_num
      
        for start,end in intervals:
        #    print("start: ", start, "end ", end)
            mp[start] = max(mp[start], end + 1)
        print(mp)
        intervals = []
      
        current_start, have = -1,-1
        # step 3 : merge overlapping intervals
        #concept - walk along a number line
        for start,end in enumerate(mp[0:]):
          #  print("start: ", start, "end: ",end, "have: ", have)
            if start <= have and end-1 >= have: #case 1: continuing the current interval
              #  print( " case a" )
                have = end-1
            elif start > have and end <= start: # case 2 : add the current interval
            #    print( " case 2 current_start:",  current_start, "end: ", end, " have: ", have )
                if current_start > -1:
                    intervals.append([current_start, have])
                current_start, have = -1,-1
            elif start > have and end > start: # case 3 : make a new interval
             #   print( " case 3 current: ", current_start, "end: ", end, " have: ", have )
                if current_start > -1:
                    
                    intervals.append([current_start, have])
                current_start, have = start,end-1

        if current_start <= have:
            intervals.append([current_start, have])
        return intervals
