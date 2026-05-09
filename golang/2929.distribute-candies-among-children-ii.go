func distributeCandies(n int, limit int) int64 {
	if 3*limit < n {
		return 0
	}

	if 3*limit == n {
		return 1
	}

	// count total combinations without limit
	// limit could be violated
	total := countCombinations(n)

	// subtract count one of the limits is violated
	// at each of three possible places
	total -= 3 * countCombinations(n-1*(limit+1))

	// add back count of two of the limits are violated
	total += 3 * countCombinations(n-2*(limit+1))

	// subtract count of three of the limits are violated
	total -= 3 * countCombinations(n-3*(limit+1))

	return total
}

// countCombinations returns the number of combinations for a given k
// C(k + 3 - 1, 3 - 1) = C(k + 2, 2) = (k + 1) * (k + 2) / 2.
func countCombinations(k int) int64 {
	if k < 0 {
		return 0
	}

	return int64(k+1) * int64(k+2) / 2
}
