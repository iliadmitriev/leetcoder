import math


class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> list[int]:
        res = [0] * num_people

        n_all = (int(math.sqrt(8 * candies + 1)) - 1) // 2
        s_all = (n_all * (n_all + 1)) // 2

        for i in range(num_people):
            n_one = n_all // num_people + (1 if i < n_all % num_people else 0)
            s_one = n_one * (2 * (i + 1) + (n_one - 1) * num_people) // 2
            res[i] += s_one

        rest = candies - s_all
        res[n_all % num_people] += rest

        return res

