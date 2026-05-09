class Solution:
    def numTeams(self, rating: list[int]) -> int:

        asc = [[0] * 4 for _ in range(len(rating))]
        dec = [[0] * 4 for _ in range(len(rating))]

        # base case: count number of increasing
        # or decreasing sequence of len == 1

        for i in range(len(rating)):
            asc[i][1] = 1
            dec[i][1] = 1

        # counts 2 and 3

        for count in range(2, 4):
            for i in range(len(rating)):
                for j in range(i + 1, len(rating)):
                    if rating[i] < rating[j]:
                        asc[i][count] += asc[j][count - 1]
                    if rating[i] > rating[j]:
                        dec[i][count] += dec[j][count - 1]

        res = 0
        for i in range(len(rating)):
            res += asc[i][3] + dec[i][3]

        return res

