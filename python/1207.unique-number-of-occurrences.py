class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        s = set()
        for k, v in Counter(arr).items():
            if v not in s:
                s.add(v)
            else:
                return False
        return True