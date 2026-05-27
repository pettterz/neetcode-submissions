class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        # count = defaultdict(int)
        # for num in nums:
        #     count[num] += 1

        res = []
        # for i in range(len(nums)):
        #     count[nums[i]] -= 1
        #     if i and nums[i] == nums[i - 1]:
        #         continue

        #     for j in range(i + 1, len(nums)):
        #         count[nums[j]] -= 1
        #         if j - 1 > i and nums[j] == nums[j - 1]:
        #             continue
        #         target = -(nums[i] + nums[j])
        #         if count[target] > 0:
        #             res.append([nums[i], nums[j], target])

        #     for j in range(i + 1, len(nums)):
        #         count[nums[j]] += 1

        n = len(nums)
        i = 0
        for i in range(0, n - 2): 
            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i - 1]:
                continue
           
            l, r = i + 1, n - 1
            while l < r:
                t = nums[i] + nums[l] + nums[r]
                if t > 0:
                    r -= 1
                elif t < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1


                
                

        

        return res