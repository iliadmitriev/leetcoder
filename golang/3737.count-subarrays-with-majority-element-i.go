func countMajoritySubarrays(nums []int, target int) int {
	n := len(nums)
	res := 0
	cnt := make(map[int]int, n)
	acc := make(map[int]int, n)

	pre := n + 1 // running prefix sum (shifted value not: -n to n, but: 0 to 2*n)
	cnt[pre]++   // count (frequency) of each running prefix
	acc[pre]++   // sum of all cnt[k], where 0 <= k <= pre

	for _, num := range nums {
		if num == target {
			pre++
		} else {
			pre--
		}

		cnt[pre]++                       // add to running frequency
		acc[pre] = acc[pre-1] + cnt[pre] // update lazy sum with previous value

		res += acc[pre-1] // add all valid subarrays ending at pre (exclusive)
	}

	return res
}