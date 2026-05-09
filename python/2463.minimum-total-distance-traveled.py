class Solution:
    def minimumTotalDistance(self, robot: list[int], factory: list[list[int]]) -> int:
        robot.sort()
        factory.sort()

        # flatten factory
        factories = []
        for _fact, _cnt in factory:
            factories.extend([_fact] * _cnt)

        robo_count = len(robot)
        fact_count = len(factories)

        dp = [[-1] * (fact_count + 1) for _ in range(robo_count + 1)]

        # set base case, all robots is fixed no matter how much factories available
        for i in range(fact_count + 1):
            dp[robo_count][i] = 0

        for i in range(robo_count - 1, -1, -1):
            for j in range(fact_count - 1, -1, -1):
                res = []

                if dp[i + 1][j + 1] >= 0:
                    res.append(dp[i + 1][j + 1] + abs(robot[i] - factories[j]))

                if dp[i][j + 1] >= 0:
                    res.append(dp[i][j + 1])

                dp[i][j] = min(res, default=-1)

        return dp[0][0]
