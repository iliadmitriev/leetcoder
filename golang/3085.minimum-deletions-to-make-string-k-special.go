func minimumDeletions(word string, k int) int {
	N := 26
	cnt := make([]int, N)
	minDeletions := len(word)
	start := 0

	for _, c := range word {
		cnt[c-'a']++
	}

	// optimize: omit leading zeros
	for start < N && cnt[start] == 0 {
		start++
	}

	for i := start; i < N; i++ {
		curDeletions := 0

		// cnt[i] is a bottom
		// cnt[i] + k is a top
		// cnt[j] is current frequency
		for j := start; j < N; j++ {
			if cnt[j] < cnt[i] {
				curDeletions += cnt[j]
			} else if cnt[j] > cnt[i]+k {
				curDeletions += cnt[j] - (cnt[i] + k)
			}
		}

		minDeletions = min(minDeletions, curDeletions)

	}

	return minDeletions
}
