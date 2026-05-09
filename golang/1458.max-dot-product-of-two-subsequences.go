
func maxDotProduct(nums1 []int, nums2 []int) int {
	a, b := maxItem(nums1), minItem(nums2)
	if a < 0 && b > 0 {
		return a * b
	}

	c, d := minItem(nums1), maxItem(nums2)
	if c > 0 && d < 0 {
		return c * d
	}

	m, n := len(nums1), len(nums2)
	var dp [][]int

	var dfs func(i, j int) int
	dfs = func(i, j int) int {
		if i == m || j == n {
			return 0
		}

		if dp[i][j] != math.MinInt {
			return dp[i][j]
		}

		dp[i][j] = max(
			nums1[i]*nums2[j]+dfs(i+1, j+1),
			max(
				dfs(i+1, j),
				dfs(i, j+1),
			),
		)

		return dp[i][j]
	}

	// dp = initMatrix(m, n, math.MinInt)
	// return dfs(0, 0)

	dp = initMatrix(m+1, n+1, 0)

	for i := m - 1; i >= 0; i-- {
		for j := n - 1; j >= 0; j-- {
			dp[i][j] = max(
				nums1[i]*nums2[j]+dp[i+1][j+1],
				max(
					dp[i+1][j],
					dp[i][j+1],
				),
			)
		}
	}

	return dp[0][0]
}

func initMatrix(m, n, init int) [][]int {
	v := make([][]int, m)
	for i := range m {
		v[i] = make([]int, n)
		for j := range n {
			v[i][j] = init
		}
	}

	return v
}

func maxItem(arr []int) int {
	m := arr[0]
	for _, v := range arr {
		m = max(m, v)
	}

	return m
}

func minItem(arr []int) int {
	m := arr[0]
	for _, v := range arr {
		m = min(m, v)
	}

	return m
}
