class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:

        collected = {5: 0, 10: 0, 20: 0}
        price = 5

        for bill in bills:
            collected[bill] += 1

            if bill == price:
                continue

            change = bill - price

            for note in [10, 5]:
                if change // note > 0 and collected[note] > 0:
                    notes = min(change // note, collected[note])
                    collected[note] -= notes
                    change -= note * notes

            if change > 0:
                return False

        return True

