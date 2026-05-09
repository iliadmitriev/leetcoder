class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """using hash generator function for window.
        """
        def gen(st: str, window: Optional[int]=None) -> Generator[int, None, None]:
            if window is None:
                window = len(st)
            n = len(st)
            h = sum(map(hash, st[:window]))
            yield h
            for i in range(window, n):
                h += hash(st[i]) - hash(st[i - window])
                yield h

        res = []

        len_s, len_p = len(s), len(p)
        if len_p > len_s:
            return res
        
        pattern = next(gen(p))
        return [i for i, curr in enumerate(gen(s, len_p)) if curr == pattern]
