func pathsWithMaxScore(board []string) []int {
	n := len(board)
	const MOD = 1_000_000_007

	type State struct {
		score int
		ways  int
	}

	dp := make([][]State, n)
	for i := range dp {
		dp[i] = make([]State, n)
		for j := range dp[i] {
			dp[i][j].score = -1
		}
	}

	dp[n-1][n-1] = State{0, 1}

	for i := n - 1; i >= 0; i-- {
		for j := n - 1; j >= 0; j-- {
			if board[i][j] == 'X' || (i == n-1 && j == n-1) {
				continue
			}

			best := -1
			ways := 0

			// predecessor came from below, right or diagonal
			for _, d := range [][2]int{{1, 0}, {0, 1}, {1, 1}} {
				pi, pj := i+d[0], j+d[1]
				if pi < n && pj < n && dp[pi][pj].score != -1 {
					s := dp[pi][pj].score
					c := dp[pi][pj].ways
					if s > best {
						best = s
						ways = c
					} else if s == best {
						ways = (ways + c) % MOD
					}
				}
			}

			if best != -1 {
				val := 0
				if board[i][j] >= '1' && board[i][j] <= '9' {
					val = int(board[i][j] - '0')
				}
        
				dp[i][j] = State{best + val, ways}
			}
		}
	}

	if dp[0][0].score == -1 {
		return []int{0, 0}
	}

	return []int{dp[0][0].score, dp[0][0].ways}
}