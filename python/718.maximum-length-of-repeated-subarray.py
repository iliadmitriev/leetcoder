class Solution(object):
    def findLength(self, A: List[int], B: List[int]):
        """Find the longest common subarray in A and B."""

        def rolling(arr: List[int], length: int) -> Iterator[Tuple[int, int]]:
            """Create generator for rolling hash.

            Args:
                arr (List[int]): input array of length grater than target length
                length (int): target length of rolling hash

            Yields:
                (Tuple(int, int)) - next hash in rolling sequence, and it's relative position.
            """
            # factor and modulo
            P, MOD = 113, 10 ** 9 + 7
            # inverted factor
            Pinv = pow(P, MOD - 2, MOD)

            if length == 0:
                yield 0, 0
                return

            # current hash and current factor raised to a power
            h, power = 0, 1
            for i, x in enumerate(arr):
                # calculate next hash
                h = (h + x * power) % MOD
                # if hash length is less than target
                if i < length - 1:
                    # increase power of factor p ** i
                    power = (power * P) % MOD
                else:
                    # otherwise, if hash length is enough
                    # return current calculated hash, and it's relative position
                    yield h, i - (length - 1)
                    # remove previous item from rolling hash
                    h = (h - arr[i - (length - 1)]) * Pinv % MOD

        def check(A: List[int], B: List[int], guess: int) -> bool:
            """Search for common subarray with length `guess`.

            Use Rabin-Karp rolling hash algorithm to find
            common subarray in input arrays.

            Args:
                A (List[int]): first list
                B (List[int]): second list
                guess: target rolling

            Returns:
                True - if there is commons sub array of length `guess`.
                False - otherwise
            """
            # build all rolling hashes of length `guess` for first list
            # hash -> list of positions
            hashes = collections.defaultdict(list)
            for ha, start in rolling(A, guess):
                hashes[ha].append(start)

            # iterate all rolling hashes of length `guess` for second list
            for hb, start in rolling(B, guess):
                # get list of positions from hashes of array A
                ha = hashes.get(hb, [])
                # if there is a match
                if any(A[i: i + guess] == B[start: start + guess] for i in ha):
                    return True
            return False

        # common length should be in between 0 and min(A.length, B.length)
        # 0 means that there is no common between A and B
        # min(A.length, B.length) - one of strings is a substring of another
        lo, hi = 0, min(len(A), len(B)) + 1
        while lo < hi:
            mi = (lo + hi) // 2
            if check(A, B, mi):
                lo = mi + 1
            else:
                hi = mi
        return lo - 1