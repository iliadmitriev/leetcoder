class Solution:
    def minimumCost(
        self,
        source: str,
        target: str,
        original: list[str],
        changed: list[str],
        cost: list[int],
    ) -> int:
        INF = int(1e9)
        N = 26
        A = ord("a")

        costMat = [[INF] * N for _ in range(N)]

        for i in range(N):
            costMat[i][i] = 0

        for _from, _to, _cost in zip(original, changed, cost):
            if costMat[ord(_from) - A][ord(_to) - A] < _cost:
                continue

            costMat[ord(_from) - A][ord(_to) - A] = _cost

        for k in range(N):
            for i in range(N):
                for j in range(N):
                    if costMat[i][k] == INF or costMat[k][j] == INF:
                        continue

                    if costMat[i][j] < costMat[i][k] + costMat[k][j]:
                        continue

                    costMat[i][j] = costMat[i][k] + costMat[k][j]

        total = 0
        for _src, _tar in zip(source, target):
            if costMat[ord(_src) - A][ord(_tar) - A] == INF:
                return -1

            total += costMat[ord(_src) - A][ord(_tar) - A]

        return total

