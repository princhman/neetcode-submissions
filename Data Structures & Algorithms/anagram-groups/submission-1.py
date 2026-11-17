class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dct = {}
        for s in strs:
            key = tuple(sorted(s))
            if key in dct:
                dct[key].append(s)
            else:
                dct[key] = [s]
        return list(dct.values())
