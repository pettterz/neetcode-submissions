class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)

        if n1 > n2:
            return False

        cnt1, cnt2 = [0] * 26, [0] * 26

        for i in range(n1):
            cnt1[ord(s1[i]) - ord('a')] += 1
            cnt2[ord(s2[i]) - ord('a')] += 1

        matches = 0
        l = 0

        for i in range(26):
            matches += 1 if cnt1[i] == cnt2[i] else 0

        for r in range(n1, n2):
            if matches == 26:
                return True

            idx = ord(s2[r]) - ord('a')

            # move right + 1
            cnt2[idx] += 1

            if cnt1[idx] == cnt2[idx]:
                matches += 1
            elif cnt1[idx] + 1 == cnt2[idx]:
                matches -= 1

            # move left + 1
            idx = ord(s2[l]) - ord('a')
            cnt2[idx] -= 1
            if cnt1[idx] == cnt2[idx]:
                matches += 1
            elif cnt1[idx] - 1 == cnt2[idx]:
                matches -= 1

            l += 1
        return matches == 26


            
        