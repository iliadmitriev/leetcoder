import (
	"strconv"
	"strings"
)

func getLucky(s string, k int) int {
	num := strings.Builder{}
	for i := 0; i < len(s); i++ {
		num.WriteString(strconv.Itoa(int(s[i] - 'a' + 1)))
	}

	nums := []byte(num.String())

	for ; k > 0; k-- {
		next := 0
		for i := 0; i < len(nums); i++ {
			next += int(nums[i] - '0')
		}

		nums = []byte(strconv.Itoa(next))
	}

	res, _ := strconv.Atoi(string(nums))
	return res
}
