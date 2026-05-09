import (
	"sort"
	"strconv"
	"strings"
)

func largestNumber(nums []int) string {
	numStr := make([]string, 0, len(nums))
	for _, num := range nums {
		numStr = append(numStr, strconv.Itoa(num))
	}

	sort.Slice(numStr, func(i, j int) bool {
		return numStr[i]+numStr[j] > numStr[j]+numStr[i]
	})

	if numStr[0] == "0" {
		return "0"
	}

	return strings.Join(numStr, "")
}
