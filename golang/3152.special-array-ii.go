func isArraySpecial(nums []int, queries [][]int) []bool {
	m, n := len(nums), len(queries)

	prev := (nums[0] + 1) % 2
	prefix := make([]int, 0, m)
	for i, num := range nums {
		if prev == num%2 {
			prefix = append(prefix, i)
		}
		prev = num % 2
	}

	result := make([]bool, 0, n)
	for _, q := range queries {
		if q[0] == q[1] {
			result = append(result, true)
		} else {
			idxLeft := searcRight(prefix, q[0])
			idxRight := searcRight(prefix, q[1])
			result = append(result, idxRight == idxLeft)
		}
	}

	return result
}

func searcRight(arr []int, target int) int {
	lo, hi := 0, len(arr)
	var mid int

	for lo < hi {
		mid = (lo + hi) / 2

		if target < arr[mid] {
			hi = mid
		} else {
			lo = mid + 1
		}
	}

	return lo
}
