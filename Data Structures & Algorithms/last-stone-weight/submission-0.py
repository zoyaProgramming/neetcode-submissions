class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        q=[-1 * stone for stone in stones]
        heapq.heapify(q)
        while len(q) > 1:
            if q[0] == q[1]:
                heapq.heappop(q)
                heapq.heappop(q)
            elif -1*q[1] < -1*q[0]:
                a= heapq.heappop(q)
                heapq.heapreplace(q, a - q[0])
        if len(q) == 1: return -1*q[0]
        return 0
