func champagneTower(poured int, query_row int, query_glass int) float64 {
    // dp[i][j] - designates how much liquid passed through
    // j-th glass in i-th row
    dp := make([][]float64, query_row + 1)
    dp[0] = make([]float64, 1)
    dp[0][0] = float64(poured)

    var left, right, left_extra, right_extra float64

    for row := 1; row <= query_row; row++ {
        dp[row] = make([]float64, row + 1)
        for col := 0; col <= row; col++ {
            // get how much liquid passed through left ancestor
            if col > 0 {
                left = dp[row - 1][col - 1]
            } else {
                left = 0.0
            }
            // get how much liquid passed through right ancestor
            if col < row {
                right = dp[row - 1][col]
            } else {
                right = 0.0
            }
            // calculate how much extra liquid passed through left and right ancestor
            left_extra = max(0.0, left - 1) // take 1 to fill glass to the edge
            right_extra = max(0.0, right - 1) // take 1 to fill glass to the edge

            // half of extra liquid will be spilled to current glass
            // and othe half to it's neighbours
            dp[row][col] = left_extra / 2 + right_extra / 2
        }
    }

    // convert how much liquid passed through the glass
    // to how much liquid left in a glass
    return min(1.0, dp[query_row][query_glass])
}

// min float64
func min(a, b float64) float64 {
    if a < b {
        return a
    }
    return b
}

// max float64
func max(a, b float64) float64 {
    if a > b {
        return a
    }
    return b
}
