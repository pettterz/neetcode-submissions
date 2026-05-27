class Solution:
    def rob(self, nums: List[int]) -> int:
        pw, pwo = 0, 0
        w, wo = 0, 0
        for i in range(len(nums)):
            w = pwo + nums[i]
            wo = max(pw, pwo)
            pwo = wo
            pw = w

        return max(w, wo)
        