class Solution:
    def matrixReshape(self, mat: list[list[int]], r: int, c: int) -> list[list[int]]:

        R, C = len(mat), len(mat[0])

        if R == r and C == c:
            return mat

        if R * C != r * c:
            return mat

        res = [[0] * c for _ in range(r)]

        for i in range(R * C):
            res[i // c][i % c] = mat[i // C][i % C]

        return res

