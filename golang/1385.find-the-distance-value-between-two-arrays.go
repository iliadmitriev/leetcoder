import "sort"

func findTheDistanceValue(arr1 []int, arr2 []int, d int) int {
	count := 0

	sort.Ints(arr2)
	for _, x := range arr1 {
		if __bisectLeft(arr2, x, d) {
			count++
		}
	}

	return count
}

func __bisectLeft(arr []int, target, diff int) bool {
	var mid int
	lo, hi := 0, len(arr)

	for lo < hi {
		mid = (lo + hi) / 2

		if arr[mid] < target {
			if target-arr[mid] <= diff {
				return false
			}

			lo = mid + 1
		} else {

			if arr[mid]-target <= diff {
				return false
			}

			hi = mid
		}

	}

	return true
}
