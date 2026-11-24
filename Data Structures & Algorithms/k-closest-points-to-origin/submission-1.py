class Solution:
    class Point():
        def __init__(self, x, y):
            self.x = x
            self.y = y
        def __lt__(self, nxt):
            return math.sqrt(pow(self.x, 2) + pow(self.y , 2)) < math.sqrt(pow(nxt.x, 2) + pow(nxt.y, 2))
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        tuplify = [self.Point(x, y) for [x,y] in points]
        lst = []
        heapq.heapify(tuplify)
        for i in range ( 0, k):
            point = heapq.heappop(tuplify)
            lst.append([point.x, point.y])
        return lst

        