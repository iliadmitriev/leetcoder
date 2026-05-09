
const inf = int64(1e18)

func maxSubarraySum(nums []int, k int) int64 {
	res := -inf
	var prev, cur int64

	prefix := make([]int64, k)
	for p := range prefix {
		prefix[p] = inf
	}
	prefix[k-1] = 0

	for i, num := range nums {
		cur += int64(num)
		prev = prefix[i%k]
		prefix[i%k] = min(prefix[i%k], cur)
		res = max(res, cur-prev)
	}

	return res
}
