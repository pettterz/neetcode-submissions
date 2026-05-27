class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # n = len(nums)
        # for i in range(n):
        #     t = target - nums[i]
        #     for j in range(i + 1, n):
        #         if nums[j] == t:
        #             return [i, j]
        # return []
        prev = {}  # val -> index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prev:
                return [prev[diff], i]
            prev[n] = i