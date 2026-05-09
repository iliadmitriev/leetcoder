import "slices"

const MOD int = 1e9 + 7

// pow modular exponentiation
func pow(base int, exp int, mod int) int {
	if mod == 1 {
		return 0
	}
	base %= mod
	res := 1
	for exp > 0 {
		if exp%2 == 1 {
			res = (res * base) % mod
		}
		exp >>= 1
		base = (base * base) % mod
	}

	return res
}

func numSubseq(nums []int, target int) int {
	total := 0

	slices.Sort(nums)

	for i, j := 0, len(nums)-1; i <= j; {
		if nums[i]+nums[j] <= target {
			total += pow(2, j-i, MOD)
			i++
		} else {
			j--
		}
	}

	return total % MOD
}
