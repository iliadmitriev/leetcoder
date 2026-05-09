func maxSum(nums []int) int {
	ma := nums[0]
	seen := make(map[int]struct{})
	pos := false
	aggPos := 0

	for _, num := range nums {
		if num >= 0 {
			pos = true
			seen[num] = struct{}{}
		} else {
			ma = max(ma, num)
		}
	}

	if !pos {
		return ma
	}

	for k := range seen {
		aggPos += k
	}

	return max(ma, aggPos)
}
