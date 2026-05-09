class Solution:
    def numberOfLines(self, widths: list[int], s: str) -> List[int]:
        pixels = 0
        lines = 1

        for c in s:
            if pixels + widths[ord(c) - ord("a")] > 100:
                pixels = widths[ord(c) - ord("a")]
                lines += 1
            else:
                pixels += widths[ord(c) - ord("a")]

        return [lines, pixels]

