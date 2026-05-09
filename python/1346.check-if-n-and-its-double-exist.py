class Solution:
    def checkIfExist(self, arr: list[int]) -> bool:
        cache: set[int] = set()

        for num in arr:
            if num * 2 in cache:
                return True

            if num % 2 == 0 and num // 2 in cache:
                return True

            cache.add(num)

        return False

