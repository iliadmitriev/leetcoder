from functools import lru_cache


class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:

        def dfs(s: str) -> int:
            n = len(s)

            @lru_cache(None)
            def dp(index: int, pprev: int, prev: int, is_less: bool, is_started: bool) -> tuple[int, int]:
                if index == n:
                    # base case: return total_waviness = 0, count_of_valid_numbers = 1
                    # 1 valid combination of 0 weavines
                    return 0, 1

                total_waviness = 0
                total_ways = 0

                max_digit = 9 if is_less else int(s[index])

                for d in range(0, max_digit + 1):
                    # if d is less than current digit
                    # it propagates downwards with is_less
                    next_less = is_less or (d < max_digit)

                    if not is_started:
                        if d == 0:
                            # case 1: continue placing leading zeroes
                            waviness, ways = dp(index + 1, -1, -1, next_less, False)
                        else:
                            # case 2: place first significant non zero digit
                            waviness, ways = dp(index + 1, -1, d, next_less, True)

                        total_waviness += waviness
                        total_ways += ways

                    else:
                        # case 3: continue building the number
                        is_wave = False

                        if pprev != -1 and prev != -1:
                            is_peak = pprev < prev > d
                            is_valley = pprev > prev < d

                            if is_peak or is_valley:
                                is_wave = True

                        sub_waviness, sub_ways = dp(index + 1, prev, d, next_less, True)

                        total_waviness += sub_waviness
                        
                        if is_wave:
                            total_waviness += sub_ways

                        total_ways += sub_ways

                return total_waviness, total_ways

            # dp.cache_clear()  
            res, _ = dp(0, -1, -1, False, False)
            return res

        res2 = dfs(str(num2))
        res1 = dfs(str(num1 - 1)) if num1 > 0 else 0

        return res2 - res1