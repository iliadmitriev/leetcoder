import "sort"

func successfulPairs(spells []int, potions []int, success int64) []int {
	n, m := len(spells), len(potions)
	res := make([]int, n)
	successInt := int(success)

	sort.Ints(potions)

	for i, spell := range spells {
		var mid int
		lo, hi := 0, m

		for lo < hi {
			mid = (lo + hi) / 2

			if spell*potions[mid] < successInt {
				lo = mid + 1
			} else {
				hi = mid
			}
		}

		res[i] = m - lo
	}

	return res
}
