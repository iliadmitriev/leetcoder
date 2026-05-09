class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        parts = []

        tmp = s.replace("-", "").upper()

        rest = len(tmp) % k

        if rest:
            parts.append(tmp[:rest])

        for i in range(rest, len(tmp), k):
            parts.append(tmp[i : i + k])

        return "-".join(parts)

