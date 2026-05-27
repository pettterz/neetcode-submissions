class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0 or n == 1:
            return n
        nums.sort()

        i, res = 0, 1

        curr = nums[0]
        curr_len = 1
        while i < n:
            if curr == nums[i] and i < n:
                i += 1

            if i >= n:
                res = max(res, curr_len)
                return res

            if curr + 1 != nums[i]:
                res = max(res, curr_len)
                curr_len = 1
                curr = nums[i]
            else:
                curr_len += 1
                curr = nums[i]

                if i == n - 1:
                    res = max(res, curr_len)
            
            i += 1
        
        return res