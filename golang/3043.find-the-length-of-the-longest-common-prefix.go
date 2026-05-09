import (
	"sort"
	"strconv"
)

func longestCommonPrefix(arr1 []int, arr2 []int) int {
	l1, l2 := len(arr1), len(arr2)
	str1, str2 := make([]string, l1), make([]string, l2)

	for i := 0; i < l1; i++ {
		str1[i] = strconv.Itoa(arr1[i])
	}

	for i := 0; i < l2; i++ {
		str2[i] = strconv.Itoa(arr2[i])
	}

	sort.Strings(str1)
	sort.Strings(str2)

	maxPrefixLen := 0

	for i, j := 0, 0; i < l1 && j < l2; {
		maxPrefixLen = max(maxPrefixLen, commonPrefixLen(str1[i], str2[j]))

		if str1[i] > str2[j] {
			j++
		} else if str1[i] < str2[j] {
			i++
		} else {
			i, j = i+1, j+1
		}
	}

	return maxPrefixLen
}

func commonPrefixLen(a, b string) int {
	n := min(len(a), len(b))
	i := 0

	for i < n && a[i] == b[i] {
		i++
	}

	return i
}
