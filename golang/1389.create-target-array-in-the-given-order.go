
import (
	"slices"
)

func createTargetArray(nums []int, index []int) []int {
	arr := make([]int, 0, len(nums))
	for i := range nums {
		arr = slices.Insert(arr, index[i], nums[i])
	}

	return arr
}
