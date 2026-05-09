class Solution:
    def checkRecord(self, s: str) -> bool:
        absent, late = 0, 0

        for att in s:
            if att == "A":
                absent += 1
                late = 0
            elif att == "L":
                late += 1
            else:
                late = 0

            if absent >= 2 or late >= 3:
                return False

        return True

