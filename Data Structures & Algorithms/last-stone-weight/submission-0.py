class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = []
        for s in stones:
            heapq.heappush(h, -s)

        while len(h) > 1:
            l1 = -heapq.heappop(h)
            l2 = -heapq.heappop(h)
            heapq.heappush(h, l2 - l1)

        res = 0
        for e in h:
            res += -e

        return res
