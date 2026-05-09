

class Solution:
    def canThreePartsEqualSum(self, arr: list[int]) -> bool:

        n = len(arr)
        total = sum(arr)

        if total % 3 != 0:
            return False

        partial = total // 3

        state = 0
        acc = 0

        for i in range(n):
            acc += arr[i]

            if acc == (state + 1) * partial:
                state += 1

            if state == 3:
                break

        return state == 3

