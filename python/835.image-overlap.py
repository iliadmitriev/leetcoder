class Solution:
    def largestOverlap(self, A: list[list[int]], B: list[list[int]]) -> int:

        dim = len(A)

        ones1, ones2 = [], []

        for i in range(dim):
            for j in range(dim):
                if A[i][j] == 1:
                    ones1.append((i, j))

                if B[i][j] == 1:
                    ones2.append((i, j))

        cnt = collections.defaultdict(int)
        for r1, c1 in ones1:
            for r2, c2 in ones2:
                delta = (r2 - r1, c2 - c1)
                cnt[delta] += 1

        return max(cnt.values(), default=0)

        # def shift_and_count(x_shift, y_shift, M, R):
        #     """
        #         Shift the matrix M in up-left and up-right directions
        #           and count the ones in the overlapping zone.
        #         M: matrix to be moved
        #         R: matrix for reference

        #         moving one matrix up is equivalent to
        #         moving the other matrix down
        #     """
        #     left_shift_count, right_shift_count = 0, 0
        #     for r_row, m_row in enumerate(range(y_shift, dim)):
        #         for r_col, m_col in enumerate(range(x_shift, dim)):
        #             if M[m_row][m_col] == 1 and M[m_row][m_col] == R[r_row][r_col]:
        #                 left_shift_count += 1
        #             if M[m_row][r_col] == 1 and M[m_row][r_col] == R[r_row][m_col]:
        #                 right_shift_count += 1

        #     return max(left_shift_count, right_shift_count)

        # max_overlaps = 0
        # # move one of the matrice up and left and vice versa.
        # # (equivalent to move the other matrix down and right)
        # for y_shift in range(0, dim):
        #     for x_shift in range(0, dim):
        #         # move the matrix A to the up-right and up-left directions
        #         max_overlaps = max(max_overlaps, shift_and_count(x_shift, y_shift, A, B))
        #         # move the matrix B to the up-right and up-left directions
        #         #  which is equivalent to moving A to the down-right and down-left directions
        #         max_overlaps = max(max_overlaps, shift_and_count(x_shift, y_shift, B, A))

        # return max_overlaps
