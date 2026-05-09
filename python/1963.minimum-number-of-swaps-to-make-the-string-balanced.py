class Solution:
    def minSwaps(self, s: str) -> int:
        swaps = 0

        w = list(s)

        n = len(s)
        i, j = 0, n - 1
        st1 = []

        while i < j:

            while i < j:
                if w[i] == "[":
                    st1.append(w[i])
                else:
                    if st1 and st1[-1] == "[":
                        st1.pop()
                    else:
                        break
                i += 1

            while i < j and w[j] == "]":
                j -= 1

            if i == j:
                break

            swaps += 1
            w[i], w[j] = w[j], w[i]

        return swaps

