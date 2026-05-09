import (
	"sort"
)

func minimumTotalDistance(robot []int, factory [][]int) int64 {
	sort.Ints(robot)
	sort.Slice(factory, func(i, j int) bool {
		return factory[i][0] < factory[j][0]
	})

	countRobots := len(robot)
	countFactories := 0
	for i := range factory {
		countFactories += factory[i][1]
	}

	// flatten factory to factories
	factories := make([]int, 0, countFactories)
	for i := range factory {
		for j := 0; j < factory[i][1]; j++ {
			factories = append(factories, factory[i][0])
		}
	}

	dp := make([][]int, countRobots+1)
	for i := range dp {
		dp[i] = make([]int, countFactories+1)
		for j := range dp[i] {
			dp[i][j] = -1
		}
	}

	// base case: all robots are fixed -> we don't need any moves (=0)
	// no matter how many factories are available
	for i := 0; i <= countFactories; i++ {
		dp[countRobots][i] = 0
	}

	for i := countRobots - 1; i >= 0; i-- {
		for j := countFactories - 1; j >= 0; j-- {
			if dp[i+1][j+1] >= 0 {
				diff := abs(robot[i] - factories[j])

				if dp[i][j] >= 0 {
					dp[i][j] = min(dp[i][j], dp[i+1][j+1]+diff)
				} else {
					dp[i][j] = dp[i+1][j+1] + diff
				}
			}

			if dp[i][j+1] >= 0 {
				if dp[i][j] >= 0 {
					dp[i][j] = min(dp[i][j], dp[i][j+1])
				} else {
					dp[i][j] = dp[i+1][j]
				}
			}
		}
	}

	return int64(dp[0][0])
}

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}
