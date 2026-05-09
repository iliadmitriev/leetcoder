class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        for v in strs[0]:
            if all((i < len(s) and s[i] == v) for s in strs[1:]):
                i += 1
            else:
                return strs[0][:i]
        return strs[0][:i]
