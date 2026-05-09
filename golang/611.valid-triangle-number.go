import "sort"

func triangleNumber(nums []int) int {
	sort.Ints(nums)
	n := len(nums)

	count := 0

	// Key observations (a, b, c indices):
	// 1) if a < b < c and a + b > c it's triangle
	// 2) if (c - 2) + (c - 1) <= c
	// two next greater elements sum is less or equal to b,
	// then there is no more triangles possible
	// 3) if 0 + 1 > c
	// if sum of two smallest elemenst is greater than c,
	// then other greater elements sum always greater than c
	// and all possible triplets combinations are triangles

	// bisectLeft := func(arr []int, target, lo, hi int) int {
	// 	var mid int
	// 	for lo < hi {
	// 		mid = (lo + hi) / 2
	//
	// 		if arr[mid] < target {
	// 			lo = mid + 1
	// 		} else {
	// 			hi = mid
	// 		}
	// 	}
	//
	// 	return lo
	// }
	//
	// for a := 0; a < n-2; a++ {
	// 	for b := a + 1; b < n-1; b++ {
	// 		// find lowest possible c index that is equal to a + b
	// 		// starting from b + 1
	// 		c := bisectLeft(nums, nums[a]+nums[b], b+1, n)
	// 		// take only possible triangles:
	// 		// all that less than c (c is equal, so -1)
	// 		count += c - b - 1
	// 	}
	// }

	for c := n - 1; c > 1; c-- {
		// optimization 1: if there are all possible triplet is a triangle
		// then there are no triangles possible
		// then count them all and break out of the loop
		if nums[0]+nums[1] > nums[c] {
			// C(x, 3) = x! / ((x - 3)! * 3!)
			// C(x, 3) = x * (x - 1) * (x - 2) / 6
			// x = c + 1
			count += (c + 1) * (c) * (c - 1) / 6
			break
		}

		// optimize 2: if theres is no possible triangles, when c is great (a + b <= c)
		// skip loop iteration to look for a smaller c
		if nums[c-2]+nums[c-1] <= nums[c] {
			continue
		}

		a, b := 0, c-1

		for a < b {
			if nums[a]+nums[b] > nums[c] {
				// all numbers between a and b - 1 (inclusive)
				// are possible triangles (a to b - 1, b, c)
				// count them and move to next b
				// mind that number of indices between x and y inclusive is y - x + 1
				// b - 1 - a + 1 => b - a
				count += b - a
				b--
			} else {
				a++
			}
		}
	}

	return count
}
