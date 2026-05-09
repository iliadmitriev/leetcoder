class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        N = len(s)

        hop = [N] * N  # next zero index, where to hop pointer
        for i in range(N - 2, -1, -1):
            if s[i + 1] == "0":
                hop[i] = i + 1
            else:
                hop[i] = hop[i + 1]

        subs = 0

        for l in range(N):
            zeros = 0
            if s[l] == "0":
                zeros = 1
            r = l

            while zeros * zeros <= N and r < N:
                n = hop[r] if r < N else N  # next zero index, non-inclusive right bound
                ones = n - l - zeros

                if ones >= zeros * zeros:
                    subs += min(
                        n - r,
                        ones - zeros * zeros + 1,
                    )

                # move to next zero and increase number zeros
                r = n
                zeros += 1

        return subs

