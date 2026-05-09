class Solution:
    def matchPlayersAndTrainers(self, players: list[int], trainers: list[int]) -> int:
        m, n = len(players), len(trainers)

        i, j = 0, 0
        count = 0

        players.sort()
        trainers.sort()

        while i < m and j < n:
            if players[i] <= trainers[j]:
                i += 1
                j += 1
                count += 1
            else:
                j += 1

        return count

