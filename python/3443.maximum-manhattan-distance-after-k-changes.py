

class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        longest = 0
        lat, lon = 0, 0

        for p, d in enumerate(s, start=1):
            if d == "N":
                lat += 1
            elif d == "S":
                lat -= 1
            elif d == "E":
                lon += 1
            elif d == "W":
                lon -= 1

            longest = max(longest, min(abs(lat) + abs(lon) + k * 2, p))

        return longest

