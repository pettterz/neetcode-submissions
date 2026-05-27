class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = {}
        for num in nums:
            cnt[num] = cnt.get(num, 0) + 1
        
        h = []
        for num, v in cnt.items():
            heapq.heappush(h, (v, num))
            if len(h) > k:
                heapq.heappop(h)

        res = []
        for i in range(k):
            _, item = heapq.heappop(h)
            res.append(item)

        return res



        
        