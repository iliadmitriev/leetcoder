class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anag = defaultdict(list)
        for word in strs:
            key = ''.join(sorted(word))
            anag[key].append(word)
        return anag.values()