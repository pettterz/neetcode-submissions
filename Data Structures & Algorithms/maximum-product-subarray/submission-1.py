class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]

        curMax, curMin = 1, 1

        for num in nums:
            if num < 0:
                t = curMin
                curMin = min(curMax * num, num)
                curMax = max(t * num, num)
            else:
                curMax = max(curMax * num, num)
                curMin = min(curMin * num, num)

            res = max(res, curMax)
        return res
        