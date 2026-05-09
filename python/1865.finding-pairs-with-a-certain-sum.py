import collections


def _gen_tests():
    import random

    n1 = 10**3
    m1 = 10**9
    d1 = [random.randint(1, m1) for _ in range(n1)]

    n2 = 10**5
    m2 = 10**5
    d2 = [random.randint(1, m2) for _ in range(n2)]

    k = 10**3
    ops = [random.random() > 0.5 for _ in range(k)]
    op: list[str] = ["FindSumPairs"]
    v: list[list[int] | list[list[int]]] = [[d1, d2]]

    for i in range(k):
        if ops[i]:
            op.append("add")
            v.append([random.randint(0, n2), random.randint(1, 100)])
        else:
            op.append("count")
            v.append([random.randint(1, m1)])

    s1 = str(op).replace("'", '"').replace(" ", "")
    s2 = str(v).replace(" ", "")

    return "\n".join([s1, s2])


class FindSumPairs:
    def __init__(self, nums1: list[int], nums2: list[int]):
        self.f1 = collections.Counter(nums1)
        self.f2 = collections.Counter(nums2)
        self.nums2 = nums2

    def add(self, index: int, val: int) -> None:
        self.f2[self.nums2[index]] -= 1
        self.f2[self.nums2[index] + val] += 1
        self.nums2[index] += val

    def count(self, tot: int) -> int:
        total = 0
        for v1, c1 in self.f1.items():
            if tot - v1 in self.f2:
                total += c1 * self.f2[tot - v1]

        return total

