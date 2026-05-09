import "math"

func minimumSubarrayLength(nums []int, k int) int {
	if k == 0 {
		return 1
	}

	n := len(nums)
	maxNum := maxArrValue(nums)

	if maxNum >= k {
		return 1
	}

	maxBits := int(math.Log2(float64(max(maxNum, k)))) + 1

	minLen := n + 1

	bitCount := make([]int, maxBits)
	cur := 0

	for left, right := 0, 0; right < n; right++ {
		num := nums[right]
		cur |= num

		for j := 0; num > 0; j++ {
			bitCount[j] += num & 1
			num >>= 1
		}

		for left <= right && cur >= k {
			minLen = min(minLen, right-left+1)

			num := nums[left]
			for j := 0; num > 0; j++ {
				bitCount[j] -= num & 1

				if bitCount[j] == 0 && (cur>>j)&1 == 1 {
					cur ^= 1 << j
				}
				num >>= 1
			}

			left++
		}
	}

	if minLen > n {
		return -1
	}

	return minLen
}

func maxArrValue(nums []int) int {
	v := nums[0]
	for _, num := range nums {
		v = max(v, num)
	}
	return v
}
