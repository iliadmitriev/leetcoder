/*
        |
      | |
    | | |
  | | | |
| | | | |
| | | | |     |
| | | | |   | |
| | | | | | | |
4 5 6 7 8 1 2 3
0 1 2 3 4 5 6 7

2
0 4 8
5 6 8
5 5 6
6 6 6
*/

func search(nums []int, target int) int {
	lo, hi := 0, len(nums)-1
	var mid int

	for lo <= hi {
		mid = (lo + hi) / 2

		// found
		if nums[mid] == target {
			return mid
		}

		if nums[mid] > nums[hi] { // right broken
			if nums[lo] <= target && target < nums[mid] { // test left part
				hi = mid - 1
			} else {
				lo = mid + 1
			}
		} else { // left broken
			if nums[mid] < target && target <= nums[hi] { // test right part
				lo = mid + 1
			} else {
				hi = mid - 1
			}
		}
	}

	return -1
}