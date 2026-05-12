class Solution:
    def minimumEffort(self, tasks: list[list[int]]) -> int:
        # sort by difference between minimal and actual amount
        # then sort by actual
        tasks.sort(key=lambda a: a[1] - a[0], reverse=True)

        cur, res = 0, 0

        for task in tasks:
            if task[1] > cur:
                diff = task[1] - cur

                cur += diff
                res += diff

            cur -= task[0]

        return res
