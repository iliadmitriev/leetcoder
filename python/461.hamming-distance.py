POPCOUNT_TABLE16 = [0] * 2 ** 16
for index in range(len(POPCOUNT_TABLE16)):
    POPCOUNT_TABLE16[index] = (index & 1) + POPCOUNT_TABLE16[index >> 1]


def popcount32_table16(v):
    return (POPCOUNT_TABLE16[v & 0xffff] +
            POPCOUNT_TABLE16[(v >> 16) & 0xffff])


class Solution:

    def hammingDistance(self, x: int, y: int) -> int:
        """ Calculate `Hamming Distance`

        The number of positions at which the corresponding bits
        of given integers are different

        Solution

        :param x: first given integer
        :param y: second given integer
        :return: number of different bits between x and y
        """
        return popcount32_table16(x ^ y)
