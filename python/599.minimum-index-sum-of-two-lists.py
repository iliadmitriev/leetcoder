class Solution:
    def findRestaurant(self, list1: list[str], list2: list[str]) -> list[str]:

        hash1 = {k: v for v, k in enumerate(list1)}
        hash2 = {k: v for v, k in enumerate(list2)}

        minIJ = int(1e9)

        for s1 in list1:
            if s1 in hash2:
                minIJ = min(minIJ, hash1[s1] + hash2[s1])

        for s2 in list2:
            if s2 in hash1:
                minIJ = min(minIJ, hash1[s2] + hash2[s2])

        res = []
        for i in range(min(len(list1), minIJ + 1)):
            j = minIJ - i

            if j < len(list2) and list1[i] == list2[j]:
                res.append(list1[i])

        return res

