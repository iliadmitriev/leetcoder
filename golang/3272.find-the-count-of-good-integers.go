
func countGoodIntegers(n int, k int) int64 {
	res := 0
	facs := make([]int, n+1)
	cache := make(map[string]struct{})
	start := powInt(10, (n-1)/2)
	end := start * 10
	cut := n % 2

	for v := start; v < end; v++ {
		palindrome := []byte(strconv.Itoa(v))
		palindrome = append(palindrome, reverseBytes(palindrome)[cut:]...)

		if v := palindromeValue(palindrome); v%k != 0 {
			continue
		}

		slices.Sort(palindrome)

		cache[string(palindrome)] = struct{}{}
	}

	// precompute factorials
	facs[0] = 1
	for i := 1; i <= n; i++ {
		facs[i] = facs[i-1] * i
	}

	for h := range cache {
		cnt := counter(h)

		res += (n - cnt[0]) * facs[n-1] / mulFactorials(cnt, facs)

	}

	return int64(res)
}

func mulFactorials(values []int, facs []int) int {
	res := 1
	for _, x := range values {
		res *= facs[x]
	}
	return res
}

func powInt(a, b int) int {
	res := 1
	for range b {
		res *= a
	}
	return res
}

func counter(s string) []int {
	res := make([]int, 10)
	for _, c := range s {
		res[c-'0']++
	}
	return res
}

func palindromeValue(x []byte) int {
	var res int
	for i := len(x) - 1; i >= 0; i-- {
		res *= 10
		res += int(x[i] - '0')
	}
	return res
}

func reverseBytes(x []byte) []byte {
	s := make([]byte, len(x))
	copy(s, x)

	for i, j := 0, len(s)-1; i < j; i, j = i+1, j-1 {
		s[i], s[j] = s[j], s[i]
	}
	return s
}
