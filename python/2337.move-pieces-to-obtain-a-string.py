

class Solution:
    def canChange(self, start: str, target: str) -> bool:

        # L >=
        # R <=

        left, right = 0, 0

        for s, t in zip(start, target):
            # open
            if s == "R":
                if left > 0:
                    return False
                right += 1

            # open
            if t == "L":
                if right > 0:
                    return False
                left += 1

            # close
            if t == "R":
                if right == 0:
                    return False
                right -= 1

            # close
            if s == "L":
                if left == 0:
                    return False
                left -= 1

        return left == 0 and right == 0

