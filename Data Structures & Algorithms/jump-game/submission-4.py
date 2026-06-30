class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0
    # def canJump(self, nums: List[int]) -> bool:
    #     n = len(nums)
    #     memo = {}

    #     def dfs(i):
    #         if i in memo:
    #             return memo[i]

    #         if i == n - 1:
    #             return True

    #         if nums[i] == 0:
    #             return False

    #         end = min(i + nums[i] + 1, n)
    #         for j in range(i + 1, end):
    #             if dfs(j):
    #                 memo[i] = True
    #                 return True

    #         memo[i] = False
    #         return False


    #     return dfs(0)