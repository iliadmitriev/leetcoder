class Solution:
    def checkValidString(self, s: str) -> bool:
        opening_min, opening_max = 0, 0
        for ch in s:
            if ch == "(":
                opening_min += 1
                opening_max += 1
            elif ch == ")":
                opening_min = max(0, opening_min - 1)
                opening_max -= 1
            else:
                opening_min = max(0, opening_min - 1)
                opening_max += 1

            if opening_max < 0:
                return False

        return opening_min == 0
