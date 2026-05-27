class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        l, r = 0, 0

        res = 0
        
        last_pos = defaultdict(int)

        while r < n:
            if s[r] in last_pos:
                l = max(l, last_pos[s[r]] + 1)

                last_pos[s[r]] = r
            else:
                last_pos[s[r]] = r
            res = max(res, r - l + 1) 
            r += 1

        return res



        