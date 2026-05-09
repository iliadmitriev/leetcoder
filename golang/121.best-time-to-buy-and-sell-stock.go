func maxProfit(prices []int) int {

	spend := prices[0]
  profit := 0

	for _, p := range prices {
		profit = max(profit, p - spend)
		spend = min(spend, p)
	}

	return profit
}