class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        res = 0

        divisors = []
        for d in range(1, math.isqrt(n) + 1):
            if n % d == 0:
                divisors.append(d)

                if n // d != d:
                    divisors.append(n // d)

        # target = sorted(nums)

        def kmp(arr1: list[int], arr2: list[int]) -> bool:
            n, m = len(arr1), len(arr2)

            pi = [0] * m
            j = 0

            for i in range(1, m):
                while j > 0 and arr2[i] != arr2[j]:
                    j = pi[j - 1]

                if arr2[i] == arr2[j]:
                    j += 1

                pi[i] = j

            j = 0
            for i in range(n):
                while j > 0 and arr1[i] != arr2[j]:
                    j = pi[j - 1]

                if arr1[i] == arr2[j]:
                    j += 1

                if j == m:
                    return True

            return False

        def cycle(arr1: list[int], arr2: list[int]) -> bool:
            n = len(arr1)

            for i in range(1, n):
                if arr1[i - 1] > arr1[i]:
                    return arr1[i:] + arr1[:i] == arr2

            return arr1 == arr2

        def check(arr1, arr2):
            return cycle(arr1, arr2)
            # return kmp(arr1 + arr1, arr2)

        # index of the first descent (nums[i] > nums[i + 1])
        # at i or onward (n if not exists)
        next_descent = [n] * n
        for i in range(n - 2, -1, -1):
            if nums[i] > nums[i + 1]:
                next_descent[i] = i  # descent starts at i
            else:
                next_descent[i] = next_descent[i + 1]  # inherit next

        # res += 1 if next_descent[0] == n else 0

        def check_is_sortable(k: int) -> bool:
            prev_last = 0

            for r in range(k - 1, n, k):
                l = r - k + 1
                drop = next_descent[l]  # first descent in window [l, r] or n

                if drop > r:
                    # case 1: window already sorted - no rotation needed.
                    # only need to connect to the previous.
                    if nums[l] < prev_last:
                        return False
                    prev_last = nums[r]
                else:
                    # case 2: window has descent at `drop`.
                    # One rotation can fix it if:
                    # a) there is no second descent (drop)
                    # b) after rotation new first value >= prev_last
                    # c) wrap around join holds nums[r] <= nums[l]
                    if (
                        next_descent[drop + 1] < r
                        or nums[drop + 1] < prev_last
                        or nums[r] > nums[l]
                    ):
                        return False

                    prev_last = nums[drop]

            return True

        for d in divisors:
            if check_is_sortable(d):
                res += d

            # for left in range(0, n, d):
            #     right = left + d

            #     if not check(nums[left:right], target[left:right]):
            #         break
            # else:
            #     res += d

        return res
