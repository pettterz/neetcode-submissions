class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        if not nums:
            return 0
        nums.sort()

        res = 1
        curr_len = 1
        for i in range(1, n):
            if nums[i] == nums[i - 1]:
                continue
            elif nums[i] == nums[i - 1] + 1:
                curr_len += 1
            else:
                res = max(res, curr_len)
                curr_len = 1 
        
        return max(res, curr_len)


        