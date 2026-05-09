class Solution:
    def tictactoe(self, moves: list[list[int]]) -> str:
        # 3 rows, 3 cols, 2 diags for player A and B
        A, B = [0] * 8, [0] * 8

        for i, (r, c) in enumerate(moves):
            P = A if i % 2 == 0 else B

            P[r] += 1
            P[3 + c] += 1

            P[6] += int(r == c)
            P[7] += int(r == 2 - c)

        for i in range(8):
            if A[i] == 3:
                return "A"
            if B[i] == 3:
                return "B"

        return "Draw" if len(moves) == 9 else "Pending"

