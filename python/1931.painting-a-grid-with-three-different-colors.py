
import numpy as np

MOD = int(1e9 + 7)


def gen_states(m: int, row: int, state: list[int]) -> list[list[int]]:
    """Generate all possible states of the grid column.

    Using backtracking to generate all possible states of the grid column.
    With constraint that no two adjacent rows should have the same color.
    """
    if row == m:
        return [state.copy()]

    res = []
    for c in range(3):
        if row > 0 and c == state[row - 1]:
            continue

        state.append(c)
        res.extend(gen_states(m, row + 1, state))
        state.pop()

    return res


def adjaceable(c1: list[int], c2: list[int]) -> bool:
    """Check if two columns of colors can be adjacent."""
    for i in range(len(c1)):
        if c1[i] == c2[i]:
            return False

    return True


def identity(k: int) -> list[list[int]]:
    """Generate square identity matrix of size k."""
    return [[1 if i == j else 0 for j in range(k)] for i in range(k)]


def mat_mul(A: list[list[int]], B: list[list[int]]) -> list[list[int]]:
    """Multiply two matrices with modulo."""
    m, n, p = len(A), len(A[0]), len(B[0])
    assert n == len(B)
    res = [[0] * p for _ in range(m)]

    for i in range(m):
        for j in range(p):
            for k in range(n):
                res[i][j] += A[i][k] * B[k][j]
                res[i][j] %= MOD

    return res


def mat_pow(A: np.ndarray, n: int) -> np.ndarray:
    """Matrix exponentiation with modulo."""
    res = np.identity(len(A), dtype=object)

    while n > 0:
        if n % 2 == 1:
            res = res @ A
            res %= MOD

        A = A @ A
        A %= MOD

        n //= 2

    return res


def build_adjacency_matrix(states: list[list[int]]) -> np.ndarray:
    """Build adjacency matrix of size len(states) for states."""
    k = len(states)
    A = np.zeros((k, k), dtype=object)

    for i in range(k):
        for j in range(k):
            if adjaceable(states[i], states[j]):
                A[i][j] = 1

    return A


class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        total = 0
        states = gen_states(m, 0, [])

        if n == 1:
            return len(states)

        adj = build_adjacency_matrix(states)
        A = mat_pow(adj, n - 1)

        for i in range(len(states)):
            for j in range(len(states)):
                total += A[i][j]
                total %= MOD

        return total

