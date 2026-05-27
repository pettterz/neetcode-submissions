class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_arr = ''.join(sorted(s))
        t_arr = ''.join(sorted(t))

        return s_arr == t_arr

        


        