import (
	"sort"
)

func canSortArray(nums []int) bool {
	n := len(nums)

	sorted := make([]int, 0, n)

	bits := popCount(nums[0])
	j := 0

	for i := 0; i < n; i++ {
		if bits != popCount(nums[i]) {
			part := make([]int, i-j)
			copy(part, nums[j:i])
			sort.Ints(part)

			sorted = append(sorted, part...)
			j = i
			bits = popCount(nums[i])
		}
	}

	if j < n {
		part := make([]int, n-j)
		copy(part, nums[j:])
		sort.Ints(part)

		sorted = append(sorted, part...)
	}

	sort.Ints(nums)

	for i := 0; i < n; i++ {
		if nums[i] != sorted[i] {
			return false
		}
	}

	return true
}

func popCount(n int) int {
	i := 0

	for n > 0 {
		n &= n - 1
		i++
	}

	return i
}
