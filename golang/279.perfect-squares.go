import (
	"math"
)

func numSquares(n int) int {
	isqrt := func(x int) int {
		return int(math.Sqrt(float64(x)))
	}

	cache := map[int]int{}

	var dfs func(int) int
	dfs = func(n int) int {
		if n < 4 {
			return n
		}
		if ret, ok := cache[n]; ok {
			return ret
		}

		v := isqrt(n)
		if v*v == n {
			return 1
		}

		k := n / (v * v)
		diff := n % (v * v)

		res := k + dfs(diff)

		for x := v - 1; x > 1; x-- {
			k := n / (x * x)
			diff = n % (x * x)

			res = min(res, k+dfs(diff))
		}

		cache[n] = res
		return res
	}

	return dfs(n)
}