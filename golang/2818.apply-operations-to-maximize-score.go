import (
	"sort"
)

func expMod(base, exp, mod int) int {
	if mod == 1 {
		return 0
	}
	res := 1
	base %= mod

	for exp > 0 {
		if exp&1 == 1 {
			res *= base
			res %= mod
		}
		base *= base
		base %= mod
		exp >>= 1
	}
	return res
}

func getPrimeScore(cache *map[int]int, num int) int {
	key := num
	if v, ok := (*cache)[key]; ok {
		return v
	}

	score := 0
	if num%2 == 0 {
		score++
	}
	for num%2 == 0 {
		num /= 2
	}

	for i := 3; i*i <= num; i += 2 {
		if num%i == 0 {
			score++
		}

		for num%i == 0 {
			num /= i
		}
	}

	if num > 2 {
		score++
	}

	(*cache)[key] = score
	return score
}

func maximumScore(nums []int, k int) int {
	n := len(nums)
	res := 1
	MOD := int(1e9 + 7)
	scores := make([]int, n)
	cache := make(map[int]int)
	indxs := make([]int, n)
	stack := make([]int, 0, n)
	left, right := make([]int, n), make([]int, n)

	for i := 0; i < n; i++ {
		indxs[i] = i
		scores[i] = getPrimeScore(&cache, nums[i])
	}

	sort.Slice(indxs, func(i, j int) bool {
		return nums[indxs[i]] > nums[indxs[j]]
	})

	stack = stack[:0]
	for i := 0; i < n; i++ {
		for len(stack) > 0 && scores[stack[len(stack)-1]] < scores[i] {
			stack = stack[:len(stack)-1]
		}

		if len(stack) > 0 {
			left[i] = stack[len(stack)-1]
		} else {
			left[i] = -1
		}

		stack = append(stack, i)
	}

	stack = stack[:0]
	for i := n - 1; i >= 0; i-- {
		for len(stack) > 0 && scores[stack[len(stack)-1]] <= scores[i] {
			stack = stack[:len(stack)-1]
		}

		if len(stack) > 0 {
			right[i] = stack[len(stack)-1]
		} else {
			right[i] = n
		}

		stack = append(stack, i)
	}

	for len(indxs) > 0 && k > 0 {
		idx := indxs[0]
		indxs = indxs[1:]

		num := nums[idx]
		l, r := idx-left[idx], right[idx]-idx
		step := min(k, l*r)

		res *= expMod(num, step, MOD)
		res %= MOD

		k -= step
	}

	return res
}
