from typing import Iterator, Tuple


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needle_hash = hash(needle)
        for i in range(len(haystack) - len(needle) + 1):
            curr_hash = hash(haystack[i: i + len(needle)])
            if curr_hash == needle_hash and needle == haystack[i: i + len(needle)]:
                return i
        return -1