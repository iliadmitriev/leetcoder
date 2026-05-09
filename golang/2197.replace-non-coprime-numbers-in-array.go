type replacer struct{}

func (r *replacer) gcd(a, b int) int {
	for b > 0 {
		a, b = b, a%b
	}

	return a
}

func (r *replacer) coprime(a, b int) bool {
	return r.gcd(a, b) == 1
}

func (r *replacer) lcm(a, b int) int {
	return a * b / r.gcd(a, b)
}

func replaceNonCoprimes(nums []int) []int {
	n := len(nums)
	r := &replacer{}

	cur := nums[0]
	res := make([]int, 0)
	res = append(res, cur)

	for i := 1; i < n; i++ {
		if r.coprime(cur, nums[i]) {
			cur = nums[i]
			res = append(res, cur)
		} else {
			cur = r.lcm(cur, nums[i])

			for len(res) > 0 && !r.coprime(cur, res[len(res)-1]) {
				cur = r.lcm(cur, res[len(res)-1])
				res = res[:len(res)-1]
			}
			res = append(res, cur)
		}
	}

	return res
}
