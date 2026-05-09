func longestIdealString(s string, k int) int {
	if k >= 26 {
		return len(s)
	}

	dp := make([]int, 26)
	for i := 0; i < len(s); i++ {
		cur := int(s[i] - 'a')

		temp := dp[cur]
		for j := max(0, cur-k); j <= min(25, cur+k); j++ {
			temp = max(temp, dp[j])
		}
		dp[cur] = temp + 1
	}

	res := dp[0]
	for j := 1; j < 26; j++ {
		res = max(res, dp[j])
	}

	return res
}
