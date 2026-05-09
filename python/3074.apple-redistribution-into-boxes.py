class Solution:
    def minimumBoxes(self, apple: list[int], capacity: list[int]) -> int:
        capacity.sort()
        totalApples = sum(apple)
        count = 0

        for i in range(len(capacity) - 1, -1, -1):
            totalApples -= capacity[i]
            count += 1

            if totalApples <= 0:
                break

        return count

