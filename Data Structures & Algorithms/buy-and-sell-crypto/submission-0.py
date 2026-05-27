class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        # diff = [0] * (n - 1)

        # for i in range(n - 2):
        #     diff[i] = prices[i + 1] - prices[i]

        # S1: sliding window
        res, tmp = 0, 0

        # l, r = 0, 1

        # while l < n and r < n:
        #     if prices[l] < prices[r]:
        #         res = max(res, prices[r] - prices[l])
        #     else:
        #         l = r
        #     r += 1
        # return res

        # S2: DP or logic
        min_price = prices[0]
        for p in prices:
            res = max(res, p - min_price)
            min_price = min(min_price, p)
        return res

        

        