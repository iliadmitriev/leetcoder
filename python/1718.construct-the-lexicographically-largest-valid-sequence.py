class Solution:

    def constructDistancedSequence(self, n: int):
        sequence = [0] * (2 * n - 1)
        used = [False] * (n + 1)

        def backtrack(index):
            if index == len(sequence):
                return True

            if sequence[index] != 0:
                return backtrack(index + 1)

            for num in range(n, 0, -1):
                if used[num]:
                    continue

                if num == 1:
                    sequence[index] = 1
                    used[1] = True
                    if backtrack(index + 1):
                        return True
                    sequence[index] = 0
                    used[1] = False
                else:
                    if index + num >= len(sequence) or sequence[index + num] != 0:
                        continue

                    sequence[index] = num
                    sequence[index + num] = num
                    used[num] = True
                    if backtrack(index + 1):
                        return True
                    sequence[index] = 0
                    sequence[index + num] = 0
                    used[num] = False

            return False

        backtrack(0)
        return sequence

