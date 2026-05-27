class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zero_cnt = 0
        for num in nums:
            if num == 0:
                zero_cnt += 1
            else:
                prod *= num

        res = [0] * len(nums)

        if zero_cnt > 1: return res

        for i, c in enumerate(nums):
            if c == 0:
                res[i] = prod
            elif zero_cnt == 0:
                res[i] = prod // c
        
        return res
        