class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if matrix is None or len(matrix[0]) == 0: return False
        outer_len, inner_len = len(matrix), len(matrix[0])
        

        # find the row:
        row_l, row_r = 0, outer_len
        row  = -1
        print("one")
        while row_l < row_r:
            mid = int((row_l + row_r)/2)
            if matrix[mid][0] <= target and target <= matrix[mid][inner_len - 1] :
                row = mid
                break
            elif target < matrix[mid][0]:
                row_r =  mid
            else:
                row_l = mid + 1
        if row == -1: return False
        # find the column
        l = 0
        r = inner_len - 1
        mid = int((l + r)/2)
        while l < r:
            
            print("row: %d col: %d"%(row, mid))
            if target == matrix[row][mid]:
                return True
            elif target < matrix[row][mid]:
                r = mid
            else:
                l = mid  + 1
            mid = int((l + r)/2)
        
        if target == matrix[row][mid]: return True
        return False