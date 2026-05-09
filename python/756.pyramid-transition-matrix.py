import collections


class Solution:
    def pyramidTransition(self, bottom: str, allowed: list[str]) -> bool:
        adj = collections.defaultdict(list)
        for a in allowed:
            adj[a[0:2]].append(a[2])

        def dp(btm: str) -> bool:
            if len(btm) == 1:
                return True

            can = [""]
            for i in range(len(btm) - 1):
                v = btm[i] + btm[i + 1]

                if v not in adj:
                    return False

                tmp = []
                for c in can:
                    for a in adj[v]:
                        tmp.append(c + a)
                can = tmp

            for c in can:
                if dp(c):
                    return True

            return False

        return dp(bottom)

