class Solution:
    def findThePrefixCommonArray(self, A: list[int], B: list[int]) -> list[int]:
        cache = set()
        count = 0
        C = []

        for a, b in zip(A, B):

            if a in cache:
                count += 1
            else:
                cache.add(a)

            if b in cache:
                count += 1
            else:
                cache.add(b)

            C.append(count)

        return C

