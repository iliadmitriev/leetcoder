import (
	"sort"
)

func numberOfPoints(nums [][]int) int {
	sort.Slice(nums, func(i, j int) bool {
		return nums[i][0] < nums[j][0] ||
			(nums[i][0] == nums[j][0] && nums[i][1] < nums[j][1])
	})

	holes := 0
	minInt := nums[0][0]
	maxInt := nums[0][1]

	for i := 1; i < len(nums); i++ {
		if maxInt < nums[i][0] {
			holes += nums[i][0] - maxInt - 1
		}

		minInt = min(minInt, nums[i][0])
		maxInt = max(maxInt, nums[i][1])
	}

	return maxInt - minInt - holes + 1
}
