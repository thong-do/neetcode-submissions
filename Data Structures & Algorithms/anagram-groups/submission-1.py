class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for i in strs:
            sorted_str = "".join(sorted(i))
            res[sorted_str].append(i)

        return list(res.values())