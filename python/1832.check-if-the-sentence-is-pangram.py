import operator
from functools import reduce

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return reduce(operator.or_, map(lambda x: 1 << (ord(x) - 97), sentence), 0) == (1 << 26) - 1