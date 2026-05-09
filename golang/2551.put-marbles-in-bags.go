import (
	"sort"
)

/*
    cases:
    1. k = 1: return 0
    2. k = 2: return max(i, (weights[0] + weights[i]) + (weights[i+1] +
            weights[n-1])) - min(i, (weights[0] + weights[i]) + (weights[i+1] +
   weights[n-1]))

        i = 0 to n - 1


    weights[0] - weights[0] + weights[n-1] - weights[n - 1] +
    max(weights[i] + weights[i+1]) - min(weights[j] + weights[j+1])

    3. k = 3:
        return max(weights[i] + weights[i+1] + weights[j] +
   weights[j+1]) - min(weights[i] + weights[i+1] + weights[j] + weights[j+1])

        i < j
        i, j = 0 to n - 1

        ....

    n. k = len(weights): return 0

*/

func putMarbles(weights []int, k int) int64 {
	n := len(weights)
	if k == 1 || k == n {
		return 0
	}

	weightPairs := make([]int, n-1)
	for i := range n - 1 {
		weightPairs[i] = weights[i] + weights[i+1]
	}

	sort.Ints(weightPairs)
	acc := func(arr []int) int {
		res := 0
		for _, v := range arr {
			res += v
		}
		return res
	}

	k-- // to get k parts we need k-1 cuts of n-1 elements
	n--
	return int64(acc(weightPairs[n-k:]) - acc(weightPairs[:k]))
}
