class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find pivot first
        n = len(nums)
        l, r = 0, n - 1

        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m

        pivot = l

        def bs(l, r):
            while l < r:
                m = l + (r - l) //2 
                if nums[m] == target:
                    return m
                elif nums[m] > target:
                    r = m
                else:
                    l = m + 1
            return -1

        res = bs(0, pivot)
        if res != -1:
            return res
        
        return bs(pivot, n)
        