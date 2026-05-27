class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        # sort by len
        sorted(strs, key=lambda x: len(x))
        # dict of sorted key with original index
        seen = {}
        for i in range(len(strs)):
            sorted_key = ''.join(sorted(strs[i]))
            seen[sorted_key] = seen.get(sorted_key, []) + [i]

        for idx in seen.values():
            group = []
            print(idx)

            for i in idx:
                group.append(strs[i])
            res.append(group)

        return res
        