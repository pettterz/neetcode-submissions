class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        res = 0

        mp = set(s)

        for c in mp:
            count = l = 0
            for r in range(n):
                if c == s[r]:
                    count += 1

                while (r - l + 1) - count > k:
                    if s[l] == c:
                        count -= 1
                    l += 1

                res = max(res, r - l + 1)


        return res


        

        