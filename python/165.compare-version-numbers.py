class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split(".")
        v2 = version2.split(".")

        n = max(len(v1), len(v2))
        for i in range(n):
            d1 = int(v1[i]) if i < len(v1) else 0
            d2 = int(v2[i]) if i < len(v2) else 0

            if d1 == d2:
                continue

            return 1 if d1 > d2 else -1

        return 0

