import operator
from itertools import accumulate


class Solution:
    def xorQueries(self, arr: list[int], queries: list[list[int]]) -> list[int]:

        prefix = list(accumulate(arr, operator.xor))

        return [prefix[i] ^ arr[i] ^ prefix[j] for i, j in queries]

