class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        res: list[list[int]] = []

        def backtrack(i: int, path: list[int], total: int) -> None:
            if total > target:
                return

            if total == target:
                res.append(path)
                return

            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue

                backtrack(j + 1, path + [candidates[j]], total + candidates[j])

        candidates.sort()
        backtrack(0, [], 0)

        return res

