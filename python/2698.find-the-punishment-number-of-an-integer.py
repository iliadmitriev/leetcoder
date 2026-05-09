class Solution:
    def isPunishmentNumber(self, num: int, target: int) -> bool:
        if num == 0 and target == 0:
            return True

        if num == 0 or target < 0:
            return False

        deg = 1
        while num // deg:
            deg *= 10

            left = num % deg

            if self.isPunishmentNumber(num // deg, target - left):
                return True

        return False

    def punishmentNumber(self, n: int) -> int:
        total = 0

        for num in range(1, n + 1):
            if self.isPunishmentNumber(num * num, num):
                total += num * num

        return total

