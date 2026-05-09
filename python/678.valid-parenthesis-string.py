class Solution:
    def checkValidString(self, s: str) -> bool:
        min_left, max_left = 0, 0

        for ch in s:
            if ch == "(":
                min_left += 1
                max_left += 1
            elif ch == ")":
                min_left = max(0, min_left - 1)
                max_left -= 1
            else:
                min_left = max(0, min_left - 1)
                max_left += 1

            if max_left < 0:
                return False

        return min_left == 0

