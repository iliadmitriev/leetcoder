func constructProductMatrix(grid [][]int) [][]int {
	/*
	   calculate prefix top to bottom for grid
	   calculate suffix bootom to top for grid moving backward (but shifted, exclusive)

	   prefix and suffix calculated as product of current value mod by constant 12345
	*/

	const MOD = 12345

	m, n := len(grid), len(grid[0])
	res := make([][]int, m) // result to be returned

	// prefix can be reduced to a single current number
	// for the purpose of algorithm the only previous value is needed
	pre := 1
	for i := range m {
		res[i] = make([]int, n)

		for j := range n {

			res[i][j] = pre

			pre = pre * grid[i][j] % MOD
		}
	}

	suf := 1
	for i := m - 1; i >= 0; i-- {
		for j := n - 1; j >= 0; j-- {

			res[i][j] = suf * res[i][j] % MOD

			suf = suf * grid[i][j] % MOD
		}
	}

	return res
}