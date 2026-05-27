class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # dict of sorted key 
        res = defaultdict(list)
        # res = {}
        for s in strs:
            sorted_key = ''.join(sorted(s))
            res[sorted_key].append(s)

        
        return list(res.values())