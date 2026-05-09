
type Pos struct {
	Y, X int
}

type StItem struct {
	Pos
	I    int
	Flag bool
}

func dfs(board [][]byte, word string, pos Pos) bool {
	m, n := len(board), len(board[0])
	st := make([]StItem, 0, m*n)
	st = append(st, StItem{pos, 0, false})

	phase := [5]int{-1, 0, 1, 0, -1}

	seen := map[Pos]bool{}

	for len(st) > 0 {
		pos, i := st[len(st)-1].Pos, st[len(st)-1].I
		flag := st[len(st)-1].Flag
		st = st[:len(st)-1]

		if flag {
			seen[pos] = false
		} else {
			if i >= len(word) {
				continue
			}

			if word[i] != board[pos.Y][pos.X] {
				continue
			}

			if i == len(word)-1 {
				return true
			}

			st = append(st, StItem{pos, i, true})
			seen[pos] = true

			for j := 0; j < 4; j++ {
				if pos.Y+phase[j] < 0 || pos.Y+phase[j] >= m || pos.X+phase[j+1] < 0 || pos.X+phase[j+1] >= n {
					continue
				}
				next := Pos{pos.Y + phase[j], pos.X + phase[j+1]}
				if seen[next] {
					continue
				}

				st = append(st, StItem{next, i + 1, false})
			}
		}
	}
	return false
}

func exist(board [][]byte, word string) bool {
	m, n := len(board), len(board[0])

	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if word[0] == board[i][j] && dfs(board, word, Pos{i, j}) {
				return true
			}
		}
	}

	return false
}
