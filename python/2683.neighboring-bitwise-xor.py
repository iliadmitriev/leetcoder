import functools as ft
import operator as op


class Solution:
    def doesValidArrayExist(self, derived: list[int]) -> bool:
        return ft.reduce(op.xor, derived) == 0

