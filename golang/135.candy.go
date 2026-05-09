func candy(ratings []int) int {
	n := len(ratings)
	candies := make([]int, n)
	res := 0

	// base
	for i := range n {
		candies[i] = 1
	}

	// left to right
	for i := 1; i < n; i++ {
		// rating of i-th is greater but the candies is less or equal then fix
		if ratings[i-1] < ratings[i] && candies[i-i] >= candies[i] {
			candies[i] = candies[i-1] + 1
		}
	}

	//right to left
	for i := n - 2; i >= 0; i-- {
		// rating of i-th is greater but the candies is less or equal then fix
		if ratings[i] > ratings[i+1] && candies[i] <= candies[i+1] {
			candies[i] = candies[i+1] + 1
		}
	}

	for _, c := range candies {
		res += c
	}

	return res
}