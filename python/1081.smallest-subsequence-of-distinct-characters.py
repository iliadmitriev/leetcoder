class Solution:
    def smallestSubsequence(self, s: str) -> str:
        M = 26

        cnt = [0] * M
        for ch in s:
            cnt[ord(ch) - 97] += 1

        st = []
        added = [False] * M

        for ch in s:
            p = ord(ch) - 97
            cnt[p] -= 1  # reduce future characters number

            # if we have current character on the stack
            # we don't need it for now, skip
            if added[p]:
                continue

            # if we have lexicographically smaller char then the character on the stack top
            # and we can replace it with the same character in the future
            # then drop it
            while st and ch < st[-1] and cnt[ord(st[-1]) - 97] > 0:
                v = st.pop()
                added[ord(v) - 97] = False

            # add character on the stack and mark it as fulfilled
            st.append(ch)
            added[p] = True

        return "".join(st)
