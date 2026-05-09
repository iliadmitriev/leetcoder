class Solution:
    @staticmethod
    def checkPrime(n: int) -> bool:
        if n == 1:
            return False
        i = 2
        while i * i <= n:
            if n % i == 0:
                return False
            i += 1
        return True

    @staticmethod
    def bsearch(arr: list[int], target: int) -> int:
        lo, hi = 0, len(arr)

        while lo < hi:
            mid = (lo + hi) // 2
            if arr[mid] < target:
                lo = mid + 1
            else:
                hi = mid

        return lo

    def primeSubOperation(self, nums: list[int]) -> bool:
        """
        1. Make first number as smaller as possible, make it 1 if it's possible
        2. Make current number nums[i] as smaller as possible but
           strictly greater then previous nums[i - 1]
           Find prime number less or equal to nums[i] - nums[i - 1] and
           subtract it from nums[i]
           otherwise, return false
        3. return true
        """
        primes = [
            0,
            2,
            3,
            5,
            7,
            11,
            13,
            17,
            19,
            23,
            29,
            31,
            37,
            41,
            43,
            47,
            53,
            59,
            61,
            67,
            71,
            73,
            79,
            83,
            89,
            97,
            101,
            103,
            107,
            109,
            113,
            127,
            131,
            137,
            139,
            149,
            151,
            157,
            163,
            167,
            173,
            179,
            181,
            191,
            193,
            197,
            199,
            211,
            223,
            227,
            229,
            233,
            239,
            241,
            251,
            257,
            263,
            269,
            271,
            277,
            281,
            283,
            293,
            307,
            311,
            313,
            317,
            331,
            337,
            347,
            349,
            353,
            359,
            367,
            373,
            379,
            383,
            389,
            397,
            401,
            409,
            419,
            421,
            431,
            433,
            439,
            443,
            449,
            457,
            461,
            463,
            467,
            479,
            487,
            491,
            499,
            503,
            509,
            521,
            523,
            541,
            547,
            557,
            563,
            569,
            571,
            577,
            587,
            593,
            599,
            601,
            607,
            613,
            617,
            619,
            631,
            641,
            643,
            647,
            653,
            659,
            661,
            673,
            677,
            683,
            691,
            701,
            709,
            719,
            727,
            733,
            739,
            743,
            751,
            757,
            761,
            769,
            773,
            787,
            797,
            809,
            811,
            821,
            823,
            827,
            829,
            839,
            853,
            857,
            859,
            863,
            877,
            881,
            883,
            887,
            907,
            911,
            919,
            929,
            937,
            941,
            947,
            953,
            967,
            971,
            977,
            983,
            991,
            997,
        ]

        prev = 0
        for num in nums:
            delta = num - prev - 1
            if delta < 0:
                return False

            pos = self.bsearch(primes, delta)
            if pos == len(primes):
                pos -= 1
            if primes[pos] > delta:
                pos -= 1

            num -= primes[pos]
            prev = num

        return True

