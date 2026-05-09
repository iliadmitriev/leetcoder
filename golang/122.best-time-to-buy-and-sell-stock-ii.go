// [7,1,5,3,6,4]
// [7,1,5,3,6,4,9]
//    b s b s   s
//      4   3   6
//b[0,7,1,5,3,6,4]
//p[0,0,4,0,3,0,5]
func maxProfit(prices []int) int {
    buy := prices[0]
    profit := 0

    for _, price := range prices {
      profit += max(0, price - buy)
      buy = price
    }

    return profit
}