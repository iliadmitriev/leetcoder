class Solution:
    def calculateTax(self, brackets: list[list[int]], income: int) -> float:

        prev, tax = 0, 0.0

        for bound, percentage in brackets:
            base = min(income, bound - prev)
            income -= base
            tax += base * percentage / 100

            prev = bound

            if income == 0:
                break

        return tax

