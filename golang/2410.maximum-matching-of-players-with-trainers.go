import "sort"

func matchPlayersAndTrainers(players []int, trainers []int) int {
	m, n := len(players), len(trainers)

	sort.Ints(players)
	sort.Ints(trainers)

	i, j := 0, 0
	count := 0
	for i < m && j < n {
		if players[i] <= trainers[j] {
			count++
			i++
		}

		j++
	}

	return count
}
