const MOD = 1e9 + 7

func zero(m, n int) [][]int {
	res := make([][]int, m)
	for i := range res {
		res[i] = make([]int, n)
	}

	return res
}

func identity(m int) [][]int {
	res := make([][]int, m)
	for i := range res {
		res[i] = make([]int, m)
		res[i][i] = 1
	}

	return res
}

// matMul computes modular matrix multiplication
func matMul(A, B [][]int) [][]int {
	m, n, p, q := len(A), len(A[0]), len(B), len(B[0])
	if n != p {
		return nil
	}

	C := zero(m, q)
	for i := range m {
		for j := range q {
			for k := range n {
				C[i][j] = (C[i][j] + A[i][k]*B[k][j]) % MOD
			}
		}
	}
	return C
}

// matExp computes modular matrix exponentiation
func matExp(A [][]int, k int) [][]int {
	res := identity(len(A))
	for k > 0 {
		if k&1 == 1 {
			res = matMul(res, A)
		}
		A = matMul(A, A)
		k >>= 1
	}
	return res
}

func checkAdjacent(c1, c2 []int) bool {
	for i := range len(c1) {
		if c1[i] == c2[i] {
			return false
		}
	}
	return true
}

func buildAdjacencyMatrix(states [][]int) [][]int {
	n := len(states)
	res := zero(n, n)

	for i := range n {
		for j := range n {
			if checkAdjacent(states[i], states[j]) {
				res[i][j] = 1
			}
		}
	}
	return res
}

func generateStates(m int, curState []int, states *[][]int) {
	if m == len(curState) {
		state := make([]int, len(curState))
		copy(state, curState)
		*states = append(*states, state)
		return
	}

	for color := range 3 {
		if len(curState) > 0 && curState[len(curState)-1] == color {
			continue
		}

		generateStates(m, append(curState, color), states)
	}
}

func colorTheGrid(m int, n int) int {
	total := 0
	states := make([][]int, 0)

	generateStates(m, make([]int, 0, m), &states)

	A := buildAdjacencyMatrix(states)

	res := matExp(A, n-1)

	for i := range states {
		for j := range states {
			total = (total + res[i][j]) % MOD
		}
	}

	return total
}
