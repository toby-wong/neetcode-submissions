class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for i in strs:
            seen.setdefault("".join(sorted(i)), []).append(i)

        return [i for i in seen.values()]