import (
	"math"
	"strconv"
)

func nearestPalindromic(n string) string {
	size := len(n)
	odd := size%2 == 1

	mid := size / 2
	if size%2 == 0 {
		mid--
	}

	left, _ := strconv.Atoi(n[:mid+1])

	candidates := []int{
		buildPalindrome(left, odd),   // 123321
		buildPalindrome(left-1, odd), // 12221
		buildPalindrome(left+1, odd), // 124421
		int(math.Pow10(size-1) - 1),  // 999999
		int(math.Pow10(size) + 1),    // 1000001
	}

	int_n, _ := strconv.Atoi(n)

	__abs := func(x int) int {
		if x < 0 {
			return -x
		}
		return x
	}

	diff := math.MaxInt
	res := 0

	for _, cand := range candidates {
		if cand == int_n {
			continue
		}

		if __abs(cand-int_n) < diff {
			diff = __abs(cand - int_n)
			res = cand

		} else if __abs(cand-int_n) == diff {
			res = min(res, cand)
		}

	}

	return strconv.Itoa(res)
}

func buildPalindrome(left int, odd bool) int {
	res := left
	if odd {
		left /= 10
	}

	for left > 0 {
		res *= 10
		res += left % 10
		left /= 10
	}

	return res
}
