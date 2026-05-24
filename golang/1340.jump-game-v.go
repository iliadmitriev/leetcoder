import (
	"cmp"
	"math"
	"slices"
)

func maxJumps(arr []int, d int) int {
	n := len(arr)
	indices := make([]int, n)
	for i := range n {
		indices[i] = i
	}

	slices.SortFunc(indices, func(i, j int) int {
		return cmp.Compare(arr[i], arr[j])
	})

	dp := make([]int, n)

	for _, i := range indices {
		h := arr[i]
		best := 0

		// scan left: i-1 .. i-d (reversed)
		maxVal := math.MinInt
		for j := i - 1; j >= max(0, i-d); j-- {
			if arr[j] >= h {
				break
			}
			if arr[j] >= maxVal {
				maxVal = arr[j]
				best = max(best, dp[j])
			}
		}

		// scan right: i+1 .. i+d
		maxVal = math.MinInt
		for j := i + 1; j < min(n, i+d+1); j++ {
			if arr[j] >= h {
				break
			}
			if arr[j] >= maxVal {
				maxVal = arr[j]
				best = max(best, dp[j])
			}
		}

		dp[i] = best + 1
	}

	return slices.Max(dp)
}