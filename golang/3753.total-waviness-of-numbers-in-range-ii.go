import (
	"fmt"
)

type Result struct {
	waviness int64
	ways     int64
}

type State struct {
	index     int
	pprev     int
	prev      int
	isLess    bool
	isStarted bool
}

func totalWaviness(num1 int64, num2 int64) int64 {


	solve := func(n int64) int64 {
		s := fmt.Sprintf("%d", n)
		length := len(s)

    // memo can't be reused for num2 and num1
    // they could have different length => different base case
    memo := make(map[State]Result)

		var dp func(int, int, int, bool, bool) Result
		dp = func(index int, pprev int, prev int, isLess bool, isStarted bool) Result {
			// Base case:
			if index == length {
				return Result{waviness: 0, ways: 1}
			}

			// cache lookup
			state := State{index, pprev, prev, isLess, isStarted}
			if res, exists := memo[state]; exists {
				return res
			}

			// iterate 0 - maxDigit

			maxDigit := 9
			if !isLess {
				maxDigit = int(s[index] - '0')
			}

			totalWaviness := int64(0)
			totalWays := int64(0)

			for d := 0; d <= maxDigit; d++ {
				nextLess := isLess || (d < maxDigit)

				if !isStarted {
					if d == 0 {
						// case 1: continue placing leading zeros
						res := dp(index+1, -1, -1, nextLess, false)
						totalWaviness += res.waviness
						totalWays += res.ways
					} else {
						// case 2: place first significant non-zero digit
						res := dp(index+1, -1, d, nextLess, true)
						totalWaviness += res.waviness
						totalWays += res.ways
					}
				} else {
					// case 3: continue building number
					isWave := false
					if pprev != -1 && prev != -1 {
						isPeak := pprev < prev && prev > d
						isValley := pprev > prev && prev < d
						isWave = isPeak || isValley
					}

					res := dp(index+1, prev, d, nextLess, true)

					// add suffix waviness
					totalWaviness += res.waviness

					// add current waviness if it's a peak or valley
					if isWave {
						totalWaviness += res.ways
					}

					totalWays += res.ways
				}
			}

			memo[state] = Result{waviness: totalWaviness, ways: totalWays}
			return memo[state]
		}

		res := dp(0, -1, -1, false, false)
		return res.waviness
	}

	res2 := solve(num2)

	var res1 int64 = 0
	if num1 > 0 {
		res1 = solve(num1 - 1)
	}

	return res2 - res1
}