import "slices"

func getWordsInLongestSubsequence(words []string, groups []int) []string {
	n := len(words)
	dp := make([]int, n)
	prev := make([]int, n)
	res := make([]string, 0)
	maxIdx, maxLen := 0, 1

	// init prev and dp
	for i := range n {
		dp[i] = 1
		prev[i] = -1
	}

	for i := range n {
		for j := range i {
			if groups[i] == groups[j] ||
				len(words[i]) != len(words[j]) ||
				hammingDistance(words[i], words[j]) != 1 {
				continue
			}

			if dp[i] < dp[j]+1 {
				dp[i] = dp[j] + 1
				prev[i] = j
			}
		}

		if dp[i] > maxLen {
			maxLen = dp[i]
			maxIdx = i
		}
	}

	for maxIdx != -1 {
		res = append(res, words[maxIdx])
		maxIdx = prev[maxIdx]
	}

	slices.Reverse(res)

	return res
}

func hammingDistance(s1, s2 string) int {
	v := 0
	for i := range len(s1) {
		if s1[i] != s2[i] {
			v++
		}
	}

	return v
}
