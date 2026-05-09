func minimumSize(nums []int, maxOperations int) int {
	total := sumItems(nums)
	count := len(nums)

	if count+maxOperations >= total {
		return 1
	}

	lo := ceilDivide(total, count+maxOperations) - 1
	hi := max(
		maxItem(nums),
		ceilDivide(total, count),
	) + 1

	var mid int

	for lo < hi {
		mid = (lo + hi) / 2

		if canDivide(nums, maxOperations, mid) {
			hi = mid
		} else {
			lo = mid + 1
		}
	}

	return hi
}

// canDivide - check if piles represented by `nums[]` can be split into parts
// not greater than `limit` with maximum number of operations `maxOperations`
func canDivide(nums []int, maxOperations, limit int) bool {
	op := 0

	for _, num := range nums {
		op += (num - 1) / limit

		if op > maxOperations {
			return false
		}
	}

	return true
}

func ceilDivide(x, y int) int {
	res := x / y
	if x%y > 0 {
		res++
	}

	return res
}

func maxItem(nums []int) int {
	res := nums[0]
	for _, v := range nums {
		if v > res {
			res = v
		}
	}

	return res
}

func sumItems(nums []int) int {
	sum := 0
	for _, v := range nums {
		sum += v
	}

	return sum
}
