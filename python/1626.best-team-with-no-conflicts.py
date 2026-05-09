class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        """Find dream team by age and score.

        dynamic programming approach
        Time: O(N^2)
        Space: O(N)
        1. zip together scores and ages
        2. sort scores and ages by age ascending then by score
        3. init with None a dp array with two N dimensions:
            previous player index and current player index
        4. start dp algorithm from 0-th current player, -1 as previous player
        4.1. on each step check if current player index have reached the end, then return 0
        4.2. if current player score is greater than previous
            - decide between take or not to take player with current index
            else:
            - do not take player with current index
        """
        data = sorted(zip(ages, scores))
        n = len(data)
        dp = [[None] * n for _ in range(n)]

        def find_dream_team(dp, data, prev: int, index: int) -> int:
            if index >= n:
                return 0

            if dp[prev + 1][index]:
                return dp[prev + 1][index]

            if prev == -1 or data[index][1] >= data[prev][1]:
                dp[prev + 1][index] = max(
                    data[index][1] + find_dream_team(dp, data, index, index + 1),
                    find_dream_team(dp, data, prev, index + 1)
                )
                return dp[prev + 1][index]
            
            dp[prev + 1][index] = find_dream_team(dp, data, prev, index + 1)
            return dp[prev + 1][index]

        return find_dream_team(dp, data, -1, 0)
